#!/usr/bin/env python3
"""Inserta en los HTML traducidos las figuras extraídas de los PDF originales.

Dos casos:
  1. Donde la traducción dejó un marcador «(Figura N: descripción)», se
     sustituye por la imagen con esa descripción como pie.
  2. Donde el texto cita una figura que no tiene marcador, la imagen se
     inserta tras el párrafo que la cita por primera vez.
"""
import html as htmlmod
import re
import shutil
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
CURSO = sys.argv[1] if len(sys.argv) > 1 else "8.03-vibraciones-ondas-es"
HTML_DIR = RAIZ / CURSO / "html"
# Salida de extraer_figuras.py, una carpeta por documento.
FIGS = Path(sys.argv[2]) if len(sys.argv) > 2 else RAIZ / "herramientas" / "figuras"
DESTINO_REL = "figuras"

# <p><em>(Figura 1.1: ... )</em></p>  — la descripción puede llevar marcado
# El paréntesis descriptivo puede ocupar el párrafo entero o llevar prosa
# detrás. La descripción nunca cruza un </p>: sin ese límite, un marcador
# sin cierre propio se comería el marcado hasta el siguiente del documento.
# El marcador puede nombrar una figura, dos unidas por «y», o un rango
# «N-M» (el libro agrupa así las secuencias de instantáneas).
MARCADOR = re.compile(
    r"<p><em>\(Figuras?\s+([0-9]+(?:\.[0-9]+)?)"      # primer número
    r"(?:\s*(y|[-–])\s*([0-9]+(?:\.[0-9]+)?))?"       # opcional: «y N» o «-N»
    r"\s*:?((?:(?!</p>|<p>).)*?)\)</em>"               # descripción
    r"(</p>|)",                                        # ¿cierra el párrafo?
    re.S)


def expandir(n1, enlace, n2, disponibles):
    """Devuelve la lista de números que nombra un marcador."""
    if not n2:
        return [n1]
    if enlace == "y":
        return [n1, n2]
    # Rango «N-M»: los intermedios solo si existen y comparten prefijo.
    pre1, _, suf1 = n1.rpartition(".")
    pre2, _, suf2 = n2.rpartition(".")
    if pre1 != pre2 or not suf1.isdigit() or not suf2.isdigit():
        return [n1, n2]
    return [f"{pre1}.{i}" for i in range(int(suf1), int(suf2) + 1)
            if f"{pre1}.{i}" in disponibles]


def figura_html(doc, nums, pie):
    imgs = []
    for n in nums:
        imgs.append(
            f'<img src="{DESTINO_REL}/{doc}/fig{n}.png" '
            f'alt="Figura {n}" loading="lazy" />')
    if len(nums) > 2:
        etiqueta = f"Figuras {nums[0]}-{nums[-1]}"
    elif len(nums) == 2:
        etiqueta = f"Figuras {nums[0]} y {nums[1]}"
    else:
        etiqueta = f"Figura {nums[0]}"
    if pie.strip():
        etiqueta += ":"
    return ('<figure class="figura">\n' + "\n".join(imgs) +
            f'\n<figcaption>{etiqueta}{pie}</figcaption>\n</figure>')


def procesar(ruta, doc):
    disponibles = {}
    if (FIGS / doc).is_dir():
        for p in sorted((FIGS / doc).glob("*.png")):
            m = re.search(r"_fig([0-9]+(?:\.[0-9]+)?)$", p.stem)
            if m:
                disponibles[m.group(1)] = p
    if not disponibles:
        return 0, 0, []

    texto = ruta.read_text(encoding="utf-8")
    if 'figure class="figura"' in texto:
        return 0, 0, []   # ya procesado: volver a pasar duplicaría las figuras
    usadas, faltan = set(), []

    def sustituir(m):
        nums = expandir(m.group(1), m.group(2), m.group(3), disponibles)
        pie = m.group(4)
        presentes = [n for n in nums if n in disponibles]
        if not presentes:
            faltan.extend(nums)
            return m.group(0)
        usadas.update(presentes)
        # Si el marcador no cerraba el párrafo, la prosa que le seguía se
        # queda suelta: hay que volver a abrirlo tras la figura.
        cierra = m.group(5)
        return figura_html(doc, presentes, pie) + ("" if cierra else "\n<p>")

    texto, n_marc = MARCADOR.subn(sustituir, texto)

    # Figuras citadas en el texto que no tenían marcador: van tras el párrafo
    # que las menciona por primera vez.
    sueltas = [n for n in disponibles if n not in usadas]
    n_extra = 0
    for num in sorted(sueltas, key=lambda s: [int(x) for x in s.split(".")]):
        cita = re.compile(r"[Ff]iguras?\s+" + re.escape(num) + r"(?![0-9.])")
        pos = None
        for m in cita.finditer(texto):
            fin = texto.find("</p>", m.end())
            if fin != -1:
                pos = fin + 4
                break
        if pos is None:
            continue
        bloque = "\n" + figura_html(doc, [num], "")
        texto = texto[:pos] + bloque + texto[pos:]
        usadas.add(num)
        n_extra += 1

    if usadas:
        destino = ruta.parent / DESTINO_REL / doc
        destino.mkdir(parents=True, exist_ok=True)
        for n in usadas:
            shutil.copy(disponibles[n], destino / f"fig{n}.png")
        ruta.write_text(texto, encoding="utf-8")

    sin_usar = sorted(set(disponibles) - usadas,
                      key=lambda s: [int(x) for x in s.split(".")])
    return n_marc, n_extra, sin_usar


if __name__ == "__main__":
    tot_m = tot_e = 0
    for ruta in sorted(HTML_DIR.glob("MIT*.html")):
        doc = ruta.stem
        m, e, sin_usar = procesar(ruta, doc)
        tot_m += m
        tot_e += e
        if m or e or sin_usar:
            resto = f"  sin ubicar={len(sin_usar)}" if sin_usar else ""
            print(f"{doc:34s} marcadores={m:<3} extra={e:<3}{resto}")
    print(f"\nTOTAL insertadas: {tot_m + tot_e}  (marcadores {tot_m}, citadas {tot_e})")
