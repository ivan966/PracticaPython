#Escribir un programa que lea un entero positivo N, 
# introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta N
# La suma de los N primeros enteros positivos puede ser calculada de la siguiente forma: suma = (n(n+1))/2

numero = int(input("ingrese un numero: "))

suma = numero*(numero+1) / 2
print(suma)


