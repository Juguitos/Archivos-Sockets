#!/bin/bash
echo "Dime el nombre de un directorio"
read ndir
  if [ -d "$ndir" ]; then
    echo "El directorio ya existe"
  else
    mkdir $ndir
    echo "El directorio ha sido creado"
  fi
