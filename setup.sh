#!/bin/bash

echo "Downloading model from Google Drive..."

FILE_ID="1UuvWbBWX2x_SdAY1VbvOgY8i5NEmccf8"
OUTPUT_DIR="./models"
OUTPUT_FILE="$OUTPUT_DIR/best.pt"

mkdir -p "$OUTPUT_DIR"

gdown "https://drive.google.com/uc?id=$FILE_ID" -O "$OUTPUT_FILE"

echo "Model has been installed: $OUTPUT_FILE"
