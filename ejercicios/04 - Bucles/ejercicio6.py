"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

*
**
***
****
*****
"""

numero = int(input("Ingrese un numero: "))
si = "*"
for i in range(numero):
    print(si*(i+1))