#!/bin/bash
function imprimir(){
  for i in  $(seq $1 $3 $2) ; do
    echo "Imprimiendo $i"
  done
}

imprimir $1 $3 $2
