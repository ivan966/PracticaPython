#Escribir un programa que pregunte el nombre en la consola y despues de que el usuario lo introduzca muestre por pantalla <nombre> tiene <n> letras, donde <nombre> es el nombre del usuario en mayusculas y <n> es el numero de letras que tiene el nombre.

nombre = input("ingrese su nombre: ")

print(f"{nombre.upper()} tiene {len(nombre)} letras")