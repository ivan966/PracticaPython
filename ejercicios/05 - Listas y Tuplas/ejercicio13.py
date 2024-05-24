"""
Escribir un programa que pregunte por una muestra de números,
separados por comas, los guarde en una lista y muestre por pantalla
su media y desviación típica.
"""

#numeros = input("ingrese numeros separados por coma (,)\n")
#numeros = numeros.split(",")
lista_pruba = [2,5,4,2,3,2,3]
suma = 0
media = 0
for i in range(len(lista_pruba)):
    suma += lista_pruba[i]
    media = suma/len(lista_pruba)

suma2=sum(lista_pruba)/len(lista_pruba)
print(media)
print(suma2)