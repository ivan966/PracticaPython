"""
Escribir un programa que cree un diccionario vacío y lo vaya llenado con
información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.)
que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
"""
datos = dict()
while True:
    clave = input("ingrese que dato que quiere ingresar, 0 para terminar\n")
    if clave == '0':
        break
    else:
        info = input(f"Ingrese el {clave}: ")
        datos[clave] = info
        print(datos)