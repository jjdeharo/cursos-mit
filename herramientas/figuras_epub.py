#!/usr/bin/env python3
"""Mete en los EPUB las mismas figuras que ya llevan los HTML.

A diferencia de la web, aquí las imágenes se guardan con fondo blanco opaco:
un lector en modo noche dejaría invisible la tinta negra sobre transparente,
y no todos respetan el CSS del libro.
"""
import io
import re
import sys
import shutil
import zipfile
from pathlib import Path

import numpy as np
from PIL import Image

RAIZ = Path(__file__).resolve().parent.parent
CURSO = RAIZ / (sys.argv[1] if len(sys.argv) > 1 else "8.03-vibraciones-ondas-es")
FIGS = Path(sys.argv[2]) if len(sys.argv) > 2 else RAIZ / "herramientas" / "figuras"

# El paréntesis descriptivo puede ocupar el párrafo entero o llevar prosa
# detrás. La descripción nunca cruza un </p>: sin ese límite, un marcador
# sin cierre propio se comería el marcado hasta el siguiente del documento.
# El marcador puede nombrar una figura, dos unidas por «y», o un rango «N-M».
MARCADOR = re.compile(
    r"<p><em>\(Figuras?\s+([0-9]+(?:\.[0-9]+)?)"      # primer número
    r"(?:\s*(y|[-–])\s*([0-9]+(?:\.[0-9]+)?))?"       # opcional: «y N» o «-N»
    r"\s*:?((?:(?!</p>|<p>).)*?)\)</em>"               # descripción
    r"(</p>|)",                                        # ¿cierra el párrafo?
    re.S)

# Los apuntes de 8.04 no llevan marcador: la leyenda ya está traducida como
# un párrafo en cursiva, «<p><em>Figura N: descripción</em></p>».
LEYENDA = re.compile(
    r"<p><em>Figuras?\s+([0-9]+(?:\.[0-9]+)?)\s*:"
    r"((?:(?!</p>).)*?)</em></p>",
    re.S)

CSS = """
/* --- figuras tomadas de los PDF originales del curso --- */
figure.figura { margin: 1.5em 0; text-align: center; page-break-inside: avoid; }
figure.figura img { max-width: 100%; height: auto; }
figure.figura figcaption {
  margin-top: 0.5em;
  font-size: 0.9em;
  font-style: italic;
  text-align: center;
}
"""


def sobre_blanco(origen):
    """Aplana la figura sobre blanco y la devuelve como PNG en memoria."""
    img = Image.open(origen).convert("RGBA")
    fondo = Image.new("RGBA", img.size, (255, 255, 255, 255))
    plano = Image.alpha_composite(fondo, img).convert("L")
    buf = io.BytesIO()
    plano.save(buf, format="PNG", optimize=True)
    return buf.getvalue()


def expandir(n1, enlace, n2, disponibles):
    """Devuelve la lista de números que nombra un marcador."""
    if not n2:
        return [n1]
    if enlace == "y":
        return [n1, n2]
    pre1, _, suf1 = n1.rpartition(".")
    pre2, _, suf2 = n2.rpartition(".")
    if pre1 != pre2 or not suf1.isdigit() or not suf2.isdigit():
        return [n1, n2]
    return [f"{pre1}.{i}" for i in range(int(suf1), int(suf2) + 1)
            if f"{pre1}.{i}" in disponibles]


def bloque(nums, pie):
    imgs = "\n".join(
        f'<img src="../images/fig{n}.png" alt="Figura {n}" />' for n in nums)
    if len(nums) > 2:
        etiqueta = f"Figuras {nums[0]}-{nums[-1]}"
    elif len(nums) == 2:
        etiqueta = f"Figuras {nums[0]} y {nums[1]}"
    else:
        etiqueta = f"Figura {nums[0]}"
    etiqueta += ":" if pie.strip() else ""
    return (f'<figure class="figura">\n{imgs}\n'
            f'<figcaption>{etiqueta}{pie}</figcaption>\n</figure>')


def procesar(epub, doc):
    dir_figs = FIGS / doc
    if not dir_figs.is_dir():
        return 0
    disponibles = {}
    for p in sorted(dir_figs.glob("*.png")):
        m = re.search(r"_fig([0-9]+(?:\.[0-9]+)?)$", p.stem)
        if m:
            disponibles[m.group(1)] = p
    if not disponibles:
        return 0

    with zipfile.ZipFile(epub) as z:
        entradas = [(i, z.read(i.filename)) for i in z.infolist()]
    nombres = {i.filename for i, _ in entradas}
    if any(n.startswith("EPUB/images/") for n in nombres):
        return 0  # ya procesado

    usadas = set()
    salida = []
    for info, datos in entradas:
        nombre = info.filename
        # No basta con buscar el marcador: hay documentos (los apuntes de
        # 8.04) que no lo llevan y solo citan las figuras en la prosa.
        if nombre.endswith(".xhtml") and re.search(rb"[Ff]iguras?\s+[0-9]", datos):
            texto = datos.decode("utf-8")

            def sub(m):
                nums = expandir(m.group(1), m.group(2), m.group(3), disponibles)
                hay = [n for n in nums if n in disponibles]
                if not hay:
                    return m.group(0)
                usadas.update(hay)
                # Si el marcador no cerraba el párrafo, hay que reabrirlo
                # para que la prosa siguiente no quede fuera de <p>.
                return bloque(hay, m.group(4)) + ("" if m.group(5) else "\n<p>")

            texto = MARCADOR.sub(sub, texto)

            def sub_leyenda(m):
                num = m.group(1)
                if num not in disponibles:
                    return m.group(0)
                usadas.add(num)
                return bloque([num], m.group(2))

            texto = LEYENDA.sub(sub_leyenda, texto)

            # Figuras citadas en el texto pero sin marcador propio.
            for num in sorted(set(disponibles) - usadas,
                              key=lambda s: [int(x) for x in s.split(".")]):
                cita = re.compile(r"[Ff]iguras?\s+" + re.escape(num) + r"(?![0-9.])")
                m = cita.search(texto)
                if not m:
                    continue
                fin = texto.find("</p>", m.end())
                if fin == -1:
                    continue
                texto = texto[:fin + 4] + "\n" + bloque([num], "") + texto[fin + 4:]
                usadas.add(num)
            datos = texto.encode("utf-8")

        elif nombre.endswith("stylesheet1.css"):
            datos = datos + CSS.encode("utf-8")

        salida.append((info, datos))

    if not usadas:
        return 0

    # Manifiesto: cada imagen necesita su <item>, y el libro deja de ser
    # solo textual para efectos de accesibilidad.
    items = "\n".join(
        f'    <item id="fig{n.replace(".", "_")}" href="images/fig{n}.png" '
        f'media-type="image/png" />' for n in sorted(usadas))
    for idx, (info, datos) in enumerate(salida):
        if info.filename.endswith(".opf"):
            s = datos.decode("utf-8")
            s = s.replace("  </manifest>", items + "\n  </manifest>")
            s = s.replace(
                '<meta property="schema:accessMode">textual</meta>',
                '<meta property="schema:accessMode">textual</meta>\n'
                '    <meta property="schema:accessMode">visual</meta>')
            salida[idx] = (info, s.encode("utf-8"))

    tmp = epub.with_suffix(".epub.tmp")
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as z:
        # mimetype va primero y sin comprimir; es requisito del formato.
        prim = [e for e in salida if e[0].filename == "mimetype"]
        resto = [e for e in salida if e[0].filename != "mimetype"]
        for info, datos in prim:
            z.writestr(zipfile.ZipInfo("mimetype"), datos,
                       compress_type=zipfile.ZIP_STORED)
        for info, datos in resto:
            z.writestr(info, datos)
        for n in sorted(usadas):
            z.writestr(f"EPUB/images/fig{n}.png", sobre_blanco(disponibles[n]))
    shutil.move(tmp, epub)
    return len(usadas)


if __name__ == "__main__":
    total = 0
    for epub in sorted((CURSO / "epubs").glob("MIT*.epub")):
        n = procesar(epub, epub.stem)
        total += n
        if n:
            print(f"{epub.stem:34s} {n} figuras")
    print(f"\nTOTAL: {total}")
