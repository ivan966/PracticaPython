#Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.

productos = input("ingrese productos separados por coma: ")

print(f"productos: \n {productos.replace(",", "\n")}")