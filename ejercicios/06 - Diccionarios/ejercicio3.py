"""
Escribir un programa que guarde en un diccionario los precios de las
frutas de la tabla, pregunte al usuario por una fruta, un número de kilos
y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta
no está en el diccionario debe mostrar un mensaje informando de ello.

fruta | precio
platano 1.35
manzana 0.80
pera 0.85
naranja 0.70
"""

frutas = {
'platano' : 1.35,
'manzana' : 0.80,
'pera' : 0.85,
'naranja' : 0.70,
}

frutaU = input('que fruta esta buscando? ')




if frutaU in frutas:
    peso = float(input('cuantos kilos? '))
    print(f'el total es: ${round(frutas[frutaU]*peso,2)}')
else:
    print(f'No se encuentra {frutaU} en el listado')