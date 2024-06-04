"""
Escribir un programa que permita gestionar la base de datos de clientes de una empresa.
Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF,
y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono,
correo, preferente), donde preferente tendrá el valor True si se trata de un cliente preferente.
El programa debe preguntar al usuario por una opción del siguiente menú: (1) Añadir cliente,
(2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes
preferentes, (6) Terminar. En función de la opción elegida el programa tendrá que hacer lo siguiente:

Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
Preguntar por el NIF del cliente y mostrar sus datos.
Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
Terminar el programa.
"""
clientes = dict()
control = ''
nif = 1
while control != '6':
    control = input('Seleccione una de las siguientes opciones:\n 1: Añadir a un cliente\n 2: Eliminar a un cliente\n 3: Mostrar Cliente\n 4: Listar todos los Clientes\n 5: Listar Clientes Preferentes\n 6: Terminar\n')
    if control == '1':
        nombre = input('Ingrese el Nombre: ')
        direccion = input('Ingrese la Direccion: ')
        telefono = input('Ingrese el Telefono: ')
        correo = input('Ingrese el Correo: ')
        vip = input('Es un Cliente Vip? (S/N)').upper()
        cliente = {
            'nombre':nombre,
            'direccion':direccion,
            'telefono':telefono,
            'correo':correo,
            'preferente': vip=='S'}
        clientes[nif]= cliente
    elif control == '2':
        nifBorrar = int(input('ingrese el codigo Nif que desea borrar: '))
        for nif in clientes:
            if nif == nifBorrar:
                del cliente[nif]
                print('El cliente a sido eliminado')
            else:
                print('Nif incorrecto')
    elif control == '3':
        clienteMostrar = int(input('Ingrese el codigo Nif del cliente a consultar: '))
        print(clientes.get(clienteMostrar,'No se encontro el Cliente'))
    elif control == '4':
        print(clientes)

