"""
Escribir un programa que almacene el abecedario en una lista,
elimine de la lista las letras que ocupen posiciones múltiplos de 3,
y muestre por pantalla la lista resultante.
"""
import string
abecedario = []
multiplosDe3 =[]
for letra in string.ascii_lowercase :
    abecedario.append(letra)
abecedario.insert(14,"ñ")
print(abecedario)

for i in range(len(abecedario),1,-1):
    if i % 3 == 0:
        abecedario.pop(i-1)
print(abecedario)
