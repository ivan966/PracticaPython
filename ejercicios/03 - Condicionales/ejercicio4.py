#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

numero = int(input("ingrese un numero: "))

if numero%2 == 0:
    print("par")
else:
    print("impar")