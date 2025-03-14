#!/bin/bash

# Verifica que se haya pasado un parámetro
if [ -z "$1" ]; then
    echo "Uso: $0 <directorio>"
    exit 1
fi

# Verifica que el directorio existe
if [ ! -d "$1" ]; then
    echo "El directorio '$1' no existe."
    exit 1
fi

# Archivo de salida
salida="atributos.txt"

# Encabezado
echo "Lista de archivos en el directorio: $1" > "$salida"
echo "----------------------------------------" >> "$salida"

# Obtener atributos de los archivos
ls -l "$1" | awk '{print "Permisos: " $1 ", Usuario: " $3 ", Grupo: " $4 ", Tamaño: " $5 " bytes, Archivo: " $9}' >> "$salida"

echo "Los atributos han sido guardados en '$salida'"
