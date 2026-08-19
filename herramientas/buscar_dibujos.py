#!/usr/bin/env python3
"""Localiza los dibujos de un PDF que no llevan leyenda «Figure N:».

extraer_figuras.py se ancla en la leyenda. Los enunciados de problemas y los
exámenes suelen intercalar un esquema sin pie, así que aquí se busca al revés:
se tapa todo lo que pdftotext reconoce como texto y lo que queda con tinta es
dibujo. El recorte final vuelve a incluir el texto que cae dentro de la banda
del dibujo, porque los rótulos (K, 2K, M...) forman parte de la figura.

    python3 buscar_dibujos.py ORIGINAL.pdf SALIDA/ [primera] [última]

Escribe SALIDA/pag<N>_<i>.png y enumera lo encontrado. La revisión es manual:
la heurística acierta con los esquemas, pero también recorta algún adorno.
"""
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

import numpy as np
from PIL import Image

DPI = 200
MIN_TINTA = 400      # píxeles de dibujo por debajo de los cuales se descarta
MIN_LADO = 60        # un recorte más pequeño que esto no es una figura
HUECO = int(0.12 * DPI)   # filas en blanco que separan dos dibujos distintos


def palabras(pdf):
    """{página: [(x0, y0, x1, y1), ...]} de las cajas de palabra, en puntos."""
    xml = subprocess.run(["pdftotext", "-bbox", str(pdf), "-"],
                         capture_output=True, text=True, check=True).stdout
    xml = re.sub(r'\sxmlns="[^"]+"', "", xml, count=1)
    # Algunos PDF arrastran caracteres de control que XML no admite.
    xml = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", "", xml)
    out = {}
    for n, pag in enumerate(ET.fromstring(xml).iter("page"), 1):
        alto = float(pag.get("height"))
        cajas = [(float(w.get("xMin")), float(w.get("yMin")),
                  float(w.get("xMax")), float(w.get("yMax")))
                 for w in pag.iter("word")]
        out[n] = (alto, cajas)
    return out


def bandas(mascara):
    """Agrupa las filas con tinta en bloques separados por huecos en blanco."""
    filas = np.where(mascara.any(axis=1))[0]
    if not len(filas):
        return []
    cortes = np.where(np.diff(filas) > HUECO)[0]
    grupos, ini = [], 0
    for c in list(cortes) + [len(filas) - 1]:
        grupos.append((filas[ini], filas[c]))
        ini = c + 1
    return grupos


def buscar(pdf, destino, desde=1, hasta=None):
    destino = Path(destino)
    destino.mkdir(parents=True, exist_ok=True)
    paginas = palabras(pdf)
    hallazgos = []
    for npag, (alto_pt, cajas) in sorted(paginas.items()):
        if npag < desde or (hasta and npag > hasta):
            continue
        salida = f"/tmp/_dib_p{npag}"
        subprocess.run(["pdftoppm", "-r", str(DPI), "-f", str(npag), "-l", str(npag),
                        "-png", "-singlefile", str(pdf), salida], check=True)
        arr = np.array(Image.open(salida + ".png").convert("L"))
        H, W = arr.shape
        esc = H / alto_pt

        tinta = arr < 245
        # Tapamos el texto, con un margen que se come antialiasing y acentos.
        solo_dibujo = tinta.copy()
        m = 3
        for x0, y0, x1, y1 in cajas:
            a, b = max(0, int(y0 * esc) - m), min(H, int(y1 * esc) + m)
            c, d = max(0, int(x0 * esc) - m), min(W, int(x1 * esc) + m)
            solo_dibujo[a:b, c:d] = False

        for arriba, abajo in bandas(solo_dibujo):
            franja = solo_dibujo[arriba:abajo + 1]
            if franja.sum() < MIN_TINTA:
                continue
            # El recorte definitivo incluye el texto de esa banda: son rótulos.
            completa = tinta[arriba:abajo + 1]
            cols = np.where(completa.any(axis=0))[0]
            mm = int(0.05 * DPI)
            t = max(0, arriba - mm)
            b = min(H, abajo + mm)
            iz = max(0, cols[0] - mm)
            de = min(W, cols[-1] + mm)
            if b - t < MIN_LADO or de - iz < MIN_LADO:
                continue
            i = sum(1 for h in hallazgos if h[1] == npag) + 1
            nombre = f"pag{npag}_{i}.png"
            Image.fromarray(arr[t:b, iz:de]).save(destino / nombre)
            hallazgos.append((nombre, npag, de - iz, b - t, int(franja.sum())))
    return hallazgos


if __name__ == "__main__":
    pdf, destino = sys.argv[1], sys.argv[2]
    desde = int(sys.argv[3]) if len(sys.argv) > 3 else 1
    hasta = int(sys.argv[4]) if len(sys.argv) > 4 else None
    for nombre, pag, w, h, tinta in buscar(pdf, destino, desde, hasta):
        print(f"{nombre:16s} pág{pag:3d}  {w}x{h}px  tinta={tinta}")
