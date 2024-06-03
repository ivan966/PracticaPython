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

#facturas = dict()
facturas = {
    '0001' : 45451,
}
valorFinal = 0
print('Bienvenido al softaware de Gestion de Facturas\n¿que desea hacer?')
while True:
    control = input((' 1: Ingresar una nueva Factura\n 2: Pagar una Factura Existente\n 3: Terminar\n'))
    #Ingreso de nuevas facturas
    if control == '1':
        clave = input('Ingrese el cod de la factura: ')
        if clave in facturas:
            print('Codigo ya existente\n\n')
            continue
        else:
            valor = input('Ingrese el precio de la Factura')
            facturas[clave] = valor
            continue
    #Pagar la factura
    elif control == '2':
        codigo = input('Ingrese el codigo de la factura a pagar: ')
        if codigo in facturas:
            cont = input(f'El valor a pagar es de {facturas.get(codigo)} desea continuar?\n').lower()
            if cont == 'si':
                valorFinal += int(facturas.get(codigo))
                continue
            else:
                continue
    elif control == '3':
        break
    else:
        print('Ingrese un numero Valido')



