"""
Escribir un programa que cree un diccionario de traducción español-inglés.
El usuario introducirá las palabras en español e inglés separadas por dos puntos,
y cada par <palabra>:<traducción> separados por comas. El programa debe crear un
diccionario con las palabras y sus traducciones. Después pedirá una frase en español
y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está
en el diccionario debe dejarla sin traducir.
"""
diccionario = dict()

palabras = input('Ingrase la plabara en español y separa por : ingrese su traduccion en ingles')

palabra_list = palabras.split(',')
for elemento in palabra_list:
    clave,valor = elemento.split(':')
    diccionario[clave]=valor

frase = input("Ingrese una frase para traducir\n")
otraFrase = frase.split(' ')
print(otraFrase)
for palabra in otraFrase:
    print(diccionario.get(otraFrase))


