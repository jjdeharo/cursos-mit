#!/usr/bin/env bash
# Genera HTML y EPUB a partir de un Markdown, con el mismo formato que el
# resto del curso: fórmulas en MathML nativo, índice, panel de lectura y
# selector de tema.
set -euo pipefail

BUILD="$(cd "$(dirname "$0")" && pwd)"
TPL="$BUILD/plantillas"
SRC="$1"                       # ruta al .md
OUT_HTML="$2"                  # ruta al .html de salida
OUT_EPUB="$3"                  # ruta al .epub de salida

# El conversor a MathML de pandoc no acepta \tag cuando lo precede una
# secuencia suelta como "2L" o "dx" (sí cuando precede una llave o un
# superíndice). Anteponer un grupo vacío lo hace válido en todos los casos.
TMP="$(mktemp --suffix=.md)"
trap 'rm -f "$TMP"' EXIT
sed 's/[[:space:]]*\\tag{/{}\\tag{/g' "$SRC" > "$TMP"
SRC="$TMP"

# --- HTML: pandoc + el "chrome" común del curso ---
pandoc "$SRC" \
  --standalone \
  --mathml \
  --toc \
  --variable=document-css= \
  --include-in-header="$TPL/head.html" \
  --include-before-body="$TPL/before.html" \
  --include-after-body="$TPL/after.html" \
  --output="$OUT_HTML"

# --- EPUB: sin el chrome (los lectores aportan sus propios ajustes) ---
pandoc "$SRC" \
  --standalone \
  --mathml \
  --toc \
  --variable=document-css= \
  --output="$OUT_EPUB"

echo "OK  $(basename "$OUT_HTML")  +  $(basename "$OUT_EPUB")"
