#!/bin/bash

CURRENT_DIR=$(pwd)

VP_APP="/Applications/Visual Paradigm.app"
PROJECT_PATH="${HOME}/Developer/IFT2935/projet/projet.vpp"
OUTPUT_PATH="${HOME}/Developer/IFT2935/projet/output"

mkdir -p "$OUTPUT_PATH"

echo "Effaçage de l'image présente..."
rm -f "$OUTPUT_PATH"/*.png

cd "${VP_APP}/Contents/Resources/app/scripts" || exit

./ExportDiagramImage.sh -project "$PROJECT_PATH" -out "$OUTPUT_PATH" -diagram "*" -type png_with_background

cd "$CURRENT_DIR" || exit

echo "Image sauvegarder à $OUTPUT_PATH"