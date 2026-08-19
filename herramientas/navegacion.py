#!/usr/bin/env python3
"""Añade a cada documento una navegación de vuelta al curso y a la portada.

Se coloca arriba, antes del título, y se repite al final del documento, que
es donde se acaba de leer y donde más molesta tener que buscar el botón
«atrás» del navegador.
"""
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
CURSOS = {
    "8.03-vibraciones-ondas-es": "8.03SC Vibraciones y Ondas",
    "8.04-fisica-cuantica-i-es": "8.04 Física Cuántica I",
}

ARRIBA = """<nav class="migas">
<a href="../../">Cursos de MIT</a> <span aria-hidden="true">›</span> <a href="../">{curso}</a>
</nav>
"""

ABAJO = """<nav class="migas migas-pie">
<a href="../">← Volver a {curso}</a>
<a href="../../">Inicio del sitio</a>
</nav>
"""


def procesar(ruta, curso):
    s = ruta.read_text(encoding="utf-8")
    if 'class="migas"' in s:
        return False

    arriba = ARRIBA.format(curso=curso)
    marca = '<header id="title-block-header">'
    if marca not in s:
        return False
    s = s.replace(marca, arriba + marca, 1)

    # Al final: justo antes del primer <script> del pie, o antes de </body>.
    abajo = ABAJO.format(curso=curso)
    m = re.search(r"\n<script>\n\(function \(\) \{", s)
    if m:
        s = s[:m.start()] + "\n" + abajo + s[m.start():]
    else:
        s = s.replace("</body>", abajo + "</body>", 1)

    ruta.write_text(s, encoding="utf-8")
    return True


if __name__ == "__main__":
    for carpeta, nombre in CURSOS.items():
        hechos = sum(procesar(p, nombre)
                     for p in sorted((RAIZ / carpeta / "html").glob("*.html")))
        print(f"{carpeta}: {hechos} documentos")
