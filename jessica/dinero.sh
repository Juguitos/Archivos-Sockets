#!/bin/bash
#De un numero dado dar cambio en monedas o en billetes

billete1000=1000
billete500=500
billete200=200
billete100=100
billete50=50
billete20=20
moneda10=10
moneda5=5
moneda2=2
moneda1=1

echo -e "Dame un numero\n"
read dinero

if [ $dinero -ge $billete1000 ] ; then
  let b1000=$dinero/$billete1000
  echo -e "Billetes de 1000: \t"$b1000
fi
#CAMBIO
let mod1000=$dinero%$billete1000

if [ $mod1000 -ge $billete500 ] ; then
  let b500=$mod1000/$billete500
  echo -e "Billetes de 500: \t"$b500
fi
#CAMBIO
let mod500=$mod1000%$billete500

if [ $mod500 -ge $billete200 ] ; then
  let b200=$mod500/$billete200
  echo -e "Billetes de 200: \t"$b200
fi
#CAMBIO
let mod200=$mod500%$billete200

if [ $mod200 -ge $billete100 ] ; then
  let b100=$mod200/$billete100
  echo -e "Billetes de 100: \t"$b100
fi
#CAMBIO
let mod100=$mod200%$billete100

if [ $mod100 -ge $billete50 ] ; then
  let b50=$mod100/$billete50
  echo -e "Billetes de 50: \t"$b50
fi
#CAMBIO
let mod50=$mod100%$billete50

if [ $mod50 -ge $billete20 ] ; then
 