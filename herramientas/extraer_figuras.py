#!/usr/bin/env python3
"""Extrae las figuras de un PDF recortándolas de la página renderizada.

Funciona tanto con figuras vectoriales como con imágenes incrustadas: en vez
de buscar objetos de imagen, localiza la leyenda ("Figure N:") mediante las
cajas de texto y recorta la tinta que queda por encima, entre la leyenda y el
bloque de texto anterior.

El PNG resultante lleva la tinta en negro sobre fondo transparente, para que
la figura se lea igual en el tema claro y en el oscuro de la web. Los EPUB
la aplanan luego sobre blanco (véase figuras_epub.py).
"""
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

import numpy as np
from PIL import Image

DPI = 200

# Por debajo de este gris el píxel se considera papel y se lleva a blanco
# puro. Los PDF vectoriales ya lo están; en los apuntes escaneados evita que
# el moteado del papel se quede como una neblina semitransparente.
BLANCO = 240


def a_transparente(gris):
    """Convierte un recorte en escala de grises a PNG de tinta transparente."""
    gris = gris.copy()
    gris[gris >= BLANCO] = 255
    rgba = np.zeros(gris.shape + (4,), dtype=np.uint8)
    rgba[..., 3] = 255 - gris          # el negro queda opaco; el papel, invisible
    return Image.fromarray(rgba, "RGBA")


def cajas_de_texto(pdf):
    """Devuelve {página: [(x0, y0, x1, y1, texto), ...]} en puntos PDF."""
    xml = subprocess.run(
        ["pdftotext", "-bbox-layout", str(pdf), "-"],
        capture_output=True, text=True, check=True).stdout
    xml = re.sub(r'\sxmlns="[^"]+"', "", xml, count=1)
    # Algunos PDF arrastran caracteres de control que XML no admite.
    xml = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", "", xml)
    raiz = ET.fromstring(xml)
    paginas = {}
    for n, pag in enumerate(raiz.iter("page"), start=1):
        w, h = float(pag.get("width")), float(pag.get("height"))
        lineas = []
        for linea in pag.iter("line"):
            txt = "".join(linea.itertext()).strip()
            if not txt:
                continue
            lineas.append((float(linea.get("xMin")), float(linea.get("yMin")),
                           float(linea.get("xMax")), float(linea.get("yMax")), txt))
        paginas[n] = (w, h, lineas)
    return paginas


def render(pdf, pagina):
    salida = f"/tmp/_fig_p{pagina}"
    subprocess.run(["pdftoppm", "-r", str(DPI), "-f", str(pagina), "-l", str(pagina),
                    "-png", "-singlefile", str(pdf), salida], check=True)
    return Image.open(salida + ".png").convert("L")


def extraer(pdf, destino, prefijo):
    destino = Path(destino)
    destino.mkdir(parents=True, exist_ok=True)
    paginas = cajas_de_texto(pdf)
    resultados = []

    # Solo son leyendas las líneas que empiezan por "Figure N:" (con dos
    # puntos); "Figure N." aparece también en medio de la prosa al citarlas.
    ES_LEYENDA = re.compile(r"^(?:Figure|Fig\.)\s*([0-9]+(?:\.[0-9]+)?)\s*:", re.I)
    mejores = {}

    for npag, (w_pt, h_pt, lineas) in paginas.items():
        leyendas = [l for l in lineas if ES_LEYENDA.match(l[4])]
        if not leyendas:
            continue
        img = render(pdf, npag)
        arr = np.array(img)
        H, W = arr.shape
        escala = H / h_pt  # px por punto
        hueco_min = int(0.30 * DPI)   # separación figura/texto: ~0,3 pulgadas

        for ley in leyendas:
            y_inf = int(ley[1] * escala)
            tinta_fila = (arr < 245).any(axis=1)

            # Subimos desde la leyenda hasta encontrar una franja en blanco
            # suficientemente ancha. Así no cortamos las gráficas que llevan
            # sus propios rótulos y ejes.
            # Fase 1: subir hasta el borde inferior de la figura, saltando el
            # hueco que la separa de la leyenda. Se arranca unos píxeles por
            # encima de la leyenda para no tropezar con su propio antialiasing.
            y = y_inf - int(0.03 * DPI)
            while y > 0 and not tinta_fila[y]:
                y -= 1
            if y <= 0:
                continue
            fondo = y + 1

            # Fase 2: seguir subiendo hasta una franja en blanco ancha, que es
            # lo que separa la figura del texto del cuerpo. Las gráficas con
            # rótulos y ejes propios se mantienen enteras.
            blancas = 0
            top = 0
            while y > 0:
                if tinta_fila[y]:
                    blancas = 0
                else:
                    blancas += 1
                    if blancas >= hueco_min:
                        top = y + blancas
                        break
                y -= 1

            # El cuerpo del texto arranca siempre en el margen izquierdo; los
            # rótulos internos de una figura van indentados. Si hay alguna
            # línea de párrafo por encima, el recorte empieza bajo ella (así
            # se descarta también la última línea corta de un párrafo).
            anchas = [l for l in lineas if (l[2] - l[0]) > 0.5 * w_pt]
            if anchas:
                margen = min(l[0] for l in anchas)
                cuerpo = [l for l in lineas
                          if abs(l[0] - margen) < 6 and l[3] * escala < fondo - 2]
                if cuerpo:
                    corte = int(max(l[3] for l in cuerpo) * escala) + int(0.05 * DPI)
                    top = max(top, corte)

            banda = arr[top:fondo, :]
            tinta = banda < 245
            if tinta.sum() < 400:
                continue
            filas = np.where(tinta.any(axis=1))[0]
            cols = np.where(tinta.any(axis=0))[0]
            m = int(0.04 * DPI)
            t = max(0, top + filas[0] - m)
            b = min(H, top + filas[-1] + m)
            iz = max(0, cols[0] - m)
            de = min(W, cols[-1] + m)
            if b - t < 40 or de - iz < 40:
                continue

            num = ES_LEYENDA.match(ley[4]).group(1)
            area = (de - iz) * (b - t)
            if num not in mejores or area > mejores[num][0]:
                mejores[num] = (area, arr[t:b, iz:de], npag, ley[4][:60],
                                de - iz, b - t)

    for num, (_, recorte, npag, texto, w, h) in sorted(
            mejores.items(), key=lambda kv: float(kv[0])):
        nombre = f"{prefijo}_fig{num}.png"
        a_transparente(recorte).save(destino / nombre)
        resultados.append((nombre, npag, texto, w, h))

    return resultados


if __name__ == "__main__":
    pdf, destino, prefijo = sys.argv[1], sys.argv[2], sys.argv[3]
    for nombre, pag, texto, w, h in extraer(pdf, destino, prefijo):
        print(f"{nombre:34s} pág{pag:3d}  {w}x{h}px  {texto}")
