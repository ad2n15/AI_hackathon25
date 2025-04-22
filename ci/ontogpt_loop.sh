#!/bin/bash

export PATH=".local/bin:$PATH"


# Set input file
INPUT_FILE="gocam-betacat_1.txt"

# Get all template names (skip header)
templates=$(ontogpt list-templates | awk 'NR>1 {print $1}')

# Loop through each template and extract
for template in $templates; do
    echo "Extracting with template: $template"
    ontogpt extract -m ollama/gemma:7b -t "$template" -i "$INPUT_FILE" > "${template}_output.json"
done

echo "✅ Extraction completed for all templates."

