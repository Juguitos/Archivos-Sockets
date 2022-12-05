#!/bin/bash
bandera=true
count=20
while [ $bandera ]
  do
  echo $count
  if [ $count -eq 1 ];
    then
    break
  fi
  ((count--))
done
