#!/bin/bash
if [ -z "$1" ]; then
    echo "Uso: ./copia_archivos.sh <nombre_archivo>"
    exit 1
fi
cp eventos.txt "$1"
echo "Se ha copiado eventos.txt en $1"
