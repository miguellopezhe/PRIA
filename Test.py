#!/usr/bin/env python3

import json

"""
fila = 5
for i in range(fila):
    print(" "*(fila-i) + "*" * (i+1))



nombre = input("Introduce nombre: ")

longitud = len(nombre)

for i in range(longitud):

    print(nombre[(longitud-i-1)], end="")

print("")

lista = [1, 2, 3, 4, 5]
longitud = len(lista)
for i in range(longitud):
      print(lista[longitud-i-1])

 
notas = [4, 7, 9, 8, 2]
longitud = len(notas)
notamax=0

for i in range(longitud):
     
     if notamax <= notas[i]:
        notamax = notas[i]
     else:
        notamax = notamax
        
print ("La nota maxima es: " + str(notamax))
"""

import datetime
fecha=str(input("Introduce la fecha (dd/MM/aaaa): "))
subcadena = fecha.split("/")
fecha_nacimiento = datetime.datetime(int(subcadena[2]), int(subcadena[1]), int(subcadena[0]))
fecha_actual = datetime.datetime.today()

diferencia = fecha_actual - fecha_nacimiento

edad = diferencia.days // 365

print(edad)