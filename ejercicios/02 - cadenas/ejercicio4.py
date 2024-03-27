#Los telefonos de una empresa tienen el siguiente formato prefijo-numero-extension donde el prefijo es el codigo del pais +34, y la extension tiene dos digitos (por ejemplo +34-987654321-56). Escribir un programa que pregunte por un numero de telefono con este formato. y muestre por pantalla el numero de telefonos sin el prefijo y la extension.

telefono = input("ingrese su numero de telefono con el prefijo y la extension: ")

print(telefono[4:-3])