#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera la versión en Markdown de un curso, pensada para dársela a una IA.

    python3 generar_markdown.py 8.03-vibraciones-ondas-es

Sale del HTML, que es el único formato que conserva el LaTeX original de cada
fórmula (dentro del MathML, en <annotation encoding="application/x-tex">). Del
PDF ese LaTeX no se puede recuperar: al extraer el texto, «\\frac{a}{b}» acaba
como caracteres sueltos y desordenados.

Antes de convertir se quita lo que no es contenido —reproductor, panel de
lectura, migas, índice de navegación, scripts— y se dejan en su lugar cosas
que el modelo sí puede aprovechar: los vídeos como enlaces a YouTube y las
figuras apuntando a su URL publicada.
"""
import glob, os, re, subprocess, sys
from bs4 import BeautifulSoup

RAIZ = os.path.dirname(os.path.abspath(__file__)) + "/.."
SITIO = "https://jjdeharo.github.io/cursos-mit/"
FUERA = ["script", "style", ".fp", ".a11y-panel", ".a11y-toggle", ".theme-toggle",
         ".migas", "#TOC", "#title-block-header"]

def convertir(curso):
    destino = os.path.join(RAIZ, curso, "markdown")
    os.makedirs(destino, exist_ok=True)
    hechos = []
    for f in sorted(glob.glob(os.path.join(RAIZ, curso, "html", "MIT*.html"))):
        sopa = BeautifulSoup(open(f).read(), "html.parser")
        for sel in FUERA:
            for el in sopa.select(sel):
                el.decompose()

        # los botones de vídeo no sobreviven al Markdown; van como enlaces
        for btn in sopa.select("button.video-play"):
            a = sopa.new_tag("a", href="https://www.youtube.com/watch?v=" + btn.get("data-vid", ""))
            a.string = btn.get("data-title", "Vídeo de la clase")
            btn.replace_with(a)
        for ext in sopa.select("a.video-ext"):   # el mismo enlace, repetido
            ext.decompose()

        # <figure> no existe en Markdown: la imagen y su pie, en dos párrafos
        for fig in sopa.select("figure.figura"):
            img = fig.find("img")
            pie = fig.find("figcaption")
            nuevo = sopa.new_tag("div")
            if img:
                p = sopa.new_tag("p")
                p.append(img.extract())
                nuevo.append(p)
            if pie:
                p = sopa.new_tag("p")
                p.extend(pie.contents)
                nuevo.append(p)
            fig.replace_with(nuevo)

        # las figuras, a su dirección publicada, para que se puedan mirar
        base = SITIO + curso + "/html/"
        for img in sopa.select("img[src]"):
            if not img["src"].startswith("http"):
                img["src"] = base + img["src"]
            # con atributos de más, pandoc deja la etiqueta HTML tal cual
            for attr in list(img.attrs):
                if attr not in ("src", "alt"):
                    del img[attr]

        tmp = os.path.join(destino, ".tmp.html")
        open(tmp, "w").write(str(sopa))
        md = os.path.join(destino, os.path.basename(f).replace(".html", ".md"))
        subprocess.run(["pandoc", tmp, "-f", "html",
                        "-t", "markdown_strict+tex_math_dollars+pipe_tables",
                        "--wrap=none", "-o", md], check=True, capture_output=True)
        os.remove(tmp)
        # pandoc deja líneas en blanco de más donde había cajas vacías
        texto = re.sub(r"\n{3,}", "\n\n", open(md).read()).strip() + "\n"
        open(md, "w").write(texto)
        hechos.append(md)
        print("OK  " + os.path.basename(md))

    # y todo el curso en un solo fichero, que es como se sube a un chat
    entero = os.path.join(destino, curso.split("-")[0].replace(".", "_") + "_curso_completo_ES.md")
    with open(entero, "w") as salida:
        salida.write("# %s — curso completo\n\n"
                     "Traducción no oficial de materiales de MIT OpenCourseWare, con asistencia\n"
                     "de IA. Licencia CC BY-NC-SA 4.0. Fórmulas en LaTeX.\n" % curso)
        for md in hechos:
            salida.write("\n\n---\n\n<!-- %s -->\n\n" % os.path.basename(md))
            salida.write(open(md).read())
    print("OK  %s  (%.1f MB)" % (os.path.basename(entero), os.path.getsize(entero) / 1e6))

if __name__ == "__main__":
    for curso in (sys.argv[1:] or ["8.03-vibraciones-ondas-es", "8.04-fisica-cuantica-i-es"]):
        convertir(curso)
