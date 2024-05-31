"""
Escribir un programa que cree un diccionario simulando una cesta de la compra.
El programa debe preguntar el artículo y su precio y añadir el par al diccionario,
hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de
la compra y el coste total, con el siguiente formato
"""

cesta = dict()
total = 0
while True:
    item = input('Ingrese lo que desea comprar, ingrese FIN para terminar\n')
    item = item.lower()
    if item == 'fin':
        break
    else:
        precio = float(input('Ingrese el precio: '))
        total += precio
        cesta[item] = precio

for producto, precio in cesta.items():
    print(f'producto: {producto} tiene un costo de {precio}')

print(f'El total de su cesta es de: {total}')