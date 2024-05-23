"""
Escribir un programa que pida al usuario una palabra y muestre por
pantalla el número de veces que contiene cada vocal.
"""
vocales = ["a","e","i","o","u"]
palabra = input("ingrese una palabra\n")

for vocal in vocales:
    con = 0
    for letra in palabra:
        if letra == vocal:
            con += 1
    print(f"la letra {vocal} sale {con} veces")