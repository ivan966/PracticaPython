"""
Escribir un programa que pregunte al usuario los números
ganadores de la lotería primitiva, los almacene en una lista
y los muestre por pantalla ordenados de menor a mayor.
"""

numerosGanadores = []

while True:
    numero = int(input("Ingrese los numeros Ganadores o 0 para terminar\n"))
    if(numero == 0):
        break
    numerosGanadores.append(numero)
numerosGanadores.sort()
print(numerosGanadores)