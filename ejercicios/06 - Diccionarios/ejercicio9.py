"""
Escribir un programa que gestione las facturas pendientes de cobro de una empresa.
Las facturas se almacenarán en un diccionario donde la clave de cada factura será el
número de factura y el valor el coste de la factura. El programa debe preguntar al usuario
si quiere añadir una nueva factura, pagar una existente o terminar. Si desea añadir una
nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario.
Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario.
Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento
y la cantidad pendiente de cobro.
"""

facturas = dict()

valorFinal = 0
totalDeuda = 0
print('Bienvenido al softaware de Gestion de Facturas\n¿que desea hacer?')
while True:
    control = input((' 1: Ingresar una nueva Factura\n 2: Pagar una Factura Existente\n 3: Terminar\n 4: Controlar facturas\n'))
    #Ingreso de nuevas facturas
    if control == '1':
        clave = input('Ingrese el cod de la factura: ')
        if clave in facturas:
            print('Codigo ya existente\n\n')
            continue
        else:
            valor = float(input('Ingrese el precio de la Factura: '))
            facturas[clave] = valor
            continue
    #Pagar la factura
    elif control == '2':
        codigo = input('Ingrese el codigo de la factura a pagar: ')
        if codigo in facturas:
            cont = input(f'El valor a pagar es de {facturas.get(codigo)} desea continuar?\n').lower()
            if cont == 'si':
                valorFinal += facturas.get(codigo)
                del facturas[codigo]
                print(facturas)
                continue
            else:
                continue
    elif control == '3':
        break
    #ver facturas
    elif control == '4':
        print(facturas)
    else:
        print('Ingrese un numero Valido')

for palabra in facturas:
    totalDeuda += facturas[palabra]

print(f'te queda un total de {len(facturas)} facturas por pagar con un monto de: {totalDeuda}$')
print(f'el total pagado es de: {valorFinal}$')



