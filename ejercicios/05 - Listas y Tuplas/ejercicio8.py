"""
Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
"""

#palabra = input("Ingresa una palabra\n")

lista = list(input("Ingrese una palabra\n"))
lista2 = lista.copy()
lista2.reverse()
if lista == lista2:
    print("es palindromo")
else:
    print("no es palindromo")