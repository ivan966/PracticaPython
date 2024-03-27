#Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y 
#un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división 
#entera respectivamente.

numero1 = int(input("ingrese un numero: "))
numero2 = int(input("ingrese un segundo numero: "))

cociente = numero1 // numero2
resto = numero1 % numero2

print(f"los numeros ingresados son {numero1} y {numero2}")
print(f"su cociente es: {cociente}")
print(f"su resto es: {resto}")