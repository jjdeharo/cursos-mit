# Herramientas

Scripts con los que se construye y mantiene el material de los cursos. Todos
se ejecutan desde esta carpeta y resuelven las rutas respecto a la raíz del
repositorio, así que no hace falta configurar nada.

## Dependencias

| Programa | Para qué |
|---|---|
| `pandoc` (3.x) | Markdown → HTML y EPUB, con las fórmulas en MathML nativo |
| `chromium` o `google-chrome` | Exportar los HTML a PDF |
| `ghostscript` (`gs`) | Comprimir los PDF resultantes |
| `poppler-utils` (`pdftotext`, `pdftoppm`) | Leer los PDF originales del MIT |
| Python 3 con `pillow` y `numpy` | Recortar y preparar las figuras |

## Flujo de trabajo

### 1. Escribir el documento

Las fuentes en Markdown están en [`fuentes/`](fuentes/). Cada una lleva su
cabecera YAML con título, autoría e idioma:

```yaml
---
title: "Examen 1 (otoño de 2016) — 8.03SC Física III: Vibraciones y Ondas"
author: "Yen-Jie Lee (traducción al español)"
lang: es
---
```

### 2. Construir HTML y EPUB

```bash
./construir.sh fuentes/MIT8.03_Examen1_ES.md \
               ../8.03-vibraciones-ondas-es/html/MIT8.03_Examen1_ES.html \
               ../8.03-vibraciones-ondas-es/epubs/MIT8.03_Examen1_ES.epub
```

El HTML se genera con el mismo «chrome» que el resto del curso —selector de
tema, panel de lectura y hoja de estilos— a partir de las plantillas de
[`plantillas/`](plantillas/). El EPUB va sin esos añadidos, porque los
lectores aportan los suyos.

> Las plantillas usan el prefijo `mit803-` para guardar los ajustes de lectura
> en `localStorage`. Para 8.04 hay que cambiarlo a `mit804-` en
> `plantillas/after.html`. El tema sí es común a todo el sitio (`mit-tema`).

### 3. Extraer las figuras de los PDF originales

```bash
python3 extraer_figuras.py ORIGINAL.pdf figuras/MIT8.03_TextCh1_ES fig
```

Localiza cada leyenda «Figure N:» y recorta la tinta que tiene encima, hasta
la primera franja en blanco ancha o hasta la última línea de párrafo. Sirve
igual para figuras vectoriales que para imágenes incrustadas, y respeta las
gráficas que llevan sus propios rótulos y ejes.

Las guarda ya como tinta opaca sobre fondo transparente, que es lo que
permite invertirlas en el tema oscuro, y lleva a blanco puro el gris muy
claro para que el moteado de los apuntes escaneados no deje neblina.

Los PDF originales no están en el repositorio. Los de 8.03 son los
`Text_ChN.pdf` del curso; los de 8.04 se sacan de la página de cada
recurso, que es donde aparece la URL con el hash:

```bash
curl -sL "https://ocw.mit.edu/courses/8-04-quantum-physics-i-spring-2016/resources/mit8_04s16_lecnotes1/" \
  | grep -oE '/courses/8-04[^"]*\.pdf' | head -1
```

Alguna figura se le escapa al recorte automático —la 8.1 y la 10.6 de
8.03—; en esos casos se localiza la página con `pdftotext -layout` y se
recorta a mano con `pdftoppm -r 200` más `Image.crop`.

### 4. Insertar las figuras

```bash
python3 insertar_figuras.py 8.03-vibraciones-ondas-es
python3 figuras_epub.py     8.03-vibraciones-ondas-es
```

El primero sustituye por la imagen los marcadores «(Figura N: descripción)»
—admite también «Figuras N y M» y el rango «Figuras N-M»— y los párrafos de
leyenda «*Figura N: descripción*», que es la forma que tienen los apuntes de
8.04; la descripción queda como pie. Las figuras que no tienen ni marcador ni
leyenda van tras el párrafo que las cita. El segundo hace lo mismo dentro de los EPUB, añadiendo
las imágenes al manifiesto; ahí van sobre fondo blanco opaco, porque un
lector en modo noche dejaría invisible la tinta negra sobre transparente.

Ambos saltan los documentos ya procesados: volver a pasarlos duplicaría las
figuras.

### 5. Navegación y PDF

```bash
python3 navegacion.py                              # migas de pan, los dos cursos
./generar_pdf.sh 8.03-vibraciones-ondas-es
```

## Comprobaciones antes de publicar

```bash
# Figuras duplicadas, pies sin cerrar o imágenes que no existen
python3 - <<'EOF'
import glob, re, os, collections
for f in sorted(glob.glob('../8.0*/html/MIT*.html')):
    s = open(f, encoding='utf-8').read()
    if s.count('<figure class="figura">') != s.count('</figure>'):
        print('figure desbalanceado:', f)
    if re.search(r'<figcaption>(?:(?!</figcaption>).)*?\)</em>', s, re.S):
        print('pie mal cerrado:', f)
    srcs = re.findall(r'<img src="([^"]+)"', s)
    for n, c in collections.Counter(srcs).items():
        if c > 1: print('imagen repetida:', f, n)
    for n in srcs:
        if not os.path.exists(os.path.join(os.path.dirname(f), n)):
            print('imagen inexistente:', f, n)
EOF

# Los EPUB deben ser XML bien formado, con mimetype primero y sin comprimir
python3 - <<'EOF'
import zipfile, glob, xml.etree.ElementTree as ET
for f in sorted(glob.glob('../8.0*/epubs/*.epub')):
    z = zipfile.ZipFile(f); i = z.infolist()[0]
    if not (i.filename == 'mimetype' and i.compress_type == zipfile.ZIP_STORED):
        print('mimetype mal:', f)
    for n in z.namelist():
        if n.endswith(('.xhtml', '.opf')):
            try: ET.fromstring(z.read(n))
            except Exception as e: print('XML mal:', f, n, e)
EOF
```

## Una advertencia

El repositorio no debería vivir dentro de una carpeta sincronizada en la
nube. Estos scripts reescriben decenas de archivos en pocos segundos y el
cliente de sincronización puede llegar a crear «conflicted copy» y revertir
cambios a medio aplicar. Ya ocurrió una vez.
