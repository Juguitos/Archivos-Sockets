#!/bin/bash
function sumar(){
  suma=0
  for i in  $(seq $1 $3 $2) ; do
    suma=$(($suma+$i))
  done
  echo $suma
}

resultado=$(sumar $1 $3 $2)
echo "El resultado de sumar los numeros del $1 al $3 con un incremento de $2 es $resultado"
