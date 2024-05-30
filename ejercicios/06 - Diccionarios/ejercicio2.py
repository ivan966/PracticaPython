"""
Escribir un programa que pregunte al usuario su nombre, edad,
dirección y teléfono y lo guarde en un diccionario. Después debe
mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en
<dirección> y su número de teléfono es <teléfono>.
"""
datos = {
    'Nombre':'',
    'Edad': '',
    'Direccion':'',
    'Telefono': '',
}
datos['Nombre'] = input('Cual es su nombre? ')
datos['Edad'] = input('Que edad tiene? ')
datos['Direccion'] = input('Cual es su direccion? ')
datos['Telefono'] = input('Ingrese su Telefono ')
print(f"{datos['Nombre']} tiene {datos['Edad']} años, vive en {datos['Direccion']} y su numero de telefono es {datos['Telefono']}")