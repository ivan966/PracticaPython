#Escribe un programa que pregunte el nombre del usuario en la consola y un numero entero e imprima por pantalla en lineas distintas el nombre del usuario tantas veces como el numero introducido.

nombre = input("ingrese su nombre: ")
numero = int(input("ingrese cantidad de veces a repetir el nombre: "))

print((nombre+ "\n") * numero)