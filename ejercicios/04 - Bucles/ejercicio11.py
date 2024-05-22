"""
Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
"""

palabra = str(input("ingrese una palabra: "))

for i in range(len(palabra)):
    print(palabra[i])


