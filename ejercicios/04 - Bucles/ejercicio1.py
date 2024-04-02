#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

palabra = input("Ingrese una palabra para repetir: ")

for i in range(10):
    print(f"{i}: {palabra}")