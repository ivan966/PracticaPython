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
clientes ={
    '0001':{
        'nombre' : 'ivan',
        'direccion' : 'adolfo carranza',
        'telefono' : '45457842',
        'correo' : 'ivanñlas',
        'preferente' : 'S'
    },
    '0002':{
        'nombre' : 'martin',
        'direccion' : 'alguna direccion',
        'telefono' : '842516',
        'correo' : 'martincito',
        'preferente' : 'N'
    },
    '0003':{
        'nombre' : 'fernanda',
        'direccion' : 'su calle',
        'telefono' : '74595',
        'correo' : 'fernandita',
        'preferente' : 'S'
    },
    '0004':{
        'nombre' : 'marcos',
        'direccion' : 'la matanza',
        'telefono' : '787872102',
        'correo' : 'marcostraba',
        'preferente' : 'N'
    }
}
#clientes = dict()
control = ''
while control != '6':
    control = input('Seleccione una de las siguientes opciones:\n 1: Añadir a un cliente\n 2: Eliminar a un cliente\n 3: Mostrar Cliente\n 4: Listar todos los Clientes\n 5: Listar Clientes Preferentes\n 6: Terminar\n')
    if control == '1':
        nif = input('Ingrese nif: ')
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
        nifBorrar = input('ingrese el codigo Nif que desea borrar: ')
        if nifBorrar in clientes:
            del clientes[nifBorrar]
        else:
            print('El Cliente no existe')
    elif control == '3':
        clienteMostrar = input('Ingrese el codigo Nif del cliente a consultar: ')
        if clienteMostrar in clientes:
            print(clienteMostrar)
    elif control == '4':
        print(clientes)
    elif control == '5':
        for cliente in clientes:
            print(clientes)
