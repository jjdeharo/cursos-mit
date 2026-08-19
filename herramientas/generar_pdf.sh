#!/usr/bin/env bash
# Exporta a PDF cada documento HTML de un curso y lo comprime.
#
#   ./generar_pdf.sh 8.03-vibraciones-ondas-es
#
# El PDF sale del propio HTML, así que hereda sus fórmulas y sus figuras. Los
# controles de pantalla y la navegación se ocultan mediante el @media print de
# estilo.css, y el tema se fuerza a claro aunque se exporte en modo oscuro.
set -euo pipefail

CURSO="${1:-8.03-vibraciones-ondas-es}"
RAIZ="$(cd "$(dirname "$0")/.." && pwd)"
HTML="$RAIZ/$CURSO/html"
PDFS="$RAIZ/$CURSO/pdfs"

[ -d "$HTML" ] || { echo "No existe $HTML" >&2; exit 1; }
mkdir -p "$PDFS"

navegador=""
for c in chromium google-chrome chromium-browser; do
  command -v "$c" >/dev/null && { navegador="$c"; break; }
done
[ -n "$navegador" ] || { echo "Hace falta chromium o google-chrome" >&2; exit 1; }

cd "$HTML"
for f in MIT*.html; do
  destino="$PDFS/${f%.html}.pdf"
  "$navegador" --headless --disable-gpu --no-sandbox --no-pdf-header-footer \
    --print-to-pdf="$destino" --virtual-time-budget=25000 \
    "file://$HTML/$f" >/dev/null 2>&1

  # Ghostscript baja el peso a la quinta parte sin pérdida apreciable; si por
  # lo que sea no mejora, se conserva el PDF original.
  if command -v gs >/dev/null; then
    gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.5 -dPDFSETTINGS=/ebook \
       -dNOPAUSE -dQUIET -dBATCH -sOutputFile="$destino.tmp" "$destino" 2>/dev/null || true
    if [ -s "$destino.tmp" ] && [ "$(stat -c%s "$destino.tmp")" -lt "$(stat -c%s "$destino")" ]; then
      mv "$destino.tmp" "$destino"
    else
      rm -f "$destino.tmp"
    fi
  fi
  echo "OK  ${f%.html}.pdf"
done
