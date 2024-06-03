"""
Escribir un programa que cree un diccionario de traducción español-inglés.
El usuario introducirá las palabras en español e inglés separadas por dos puntos,
y cada par <palabra>:<traducción> separados por comas. El programa debe crear un
diccionario con las palabras y sus traducciones. Después pedirá una frase en español
y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está
en el diccionario debe dejarla sin traducir.
"""
#definimos el diccionario
diccionario = dict()
#el usuario ingresa la lista
palabras = input('Ingrase la plabara en español y separa por : ingrese su traduccion en ingles\n')
#todas las frases en minusculas
palabras = palabras.lower()
#separamos toda la cadena te texto donde esta la coma y lo hacemos una lista
palabraLista = palabras.split(',')
#recorremos la lista y separamos las palabras donde estan los : (dos puntos)
for elemento in palabraLista:
    #ponemos cada valor en las 2 siguientes variables
    clave,valor = elemento.split(':')
    #agregamos los valores de las variables al diccionario
    diccionario[clave]=valor
#el usuario ingresa la frase a traducir
frase = input("Ingrese una frase para traducir\n")
#toda la frase en minusculas
frase = frase.lower()
#dividimos la frase en una lista
fraseLista = frase.split(' ')

fraseFinal = ''
for frase in fraseLista:
    fraseFinal += diccionario.get(frase, frase) + ' '
print(fraseFinal)