"""
Escribir un programa que pregunte por una muestra de números,
separados por comas, los guarde en una lista y muestre por pantalla
su media y desviación típica.
"""
import math
#numeros = input("ingrese numeros separados por coma (,)\n")
#numeros = numeros.split(",")
lista_pruba = [1,2,3,4,5]
len_lista = len(lista_pruba)
for i in range(len(lista_pruba)):
    lista_pruba[i] = int(lista_pruba[i])
n = len(lista_pruba)
suma = 0
des = 0

for i in lista_pruba:
    suma += i
    des += i**2

media = suma / n

desviacion = (des/n-media**2)**(1/2)

print(f"media {media}")
print(f"desviacion {desviacion}")