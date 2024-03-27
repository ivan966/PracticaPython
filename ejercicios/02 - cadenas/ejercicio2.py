#Escribir un programa que pregunte el nombre completo del usuario en la consola y despues muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minusculas, otra con todas las letras mayusculas y otra solo con la primera letra del nombre y de los apellidos en mayuscula. el usuario puede introducir su nombre combinando mayusculas y minusculas como quiera.

nombre = input("ingrese su nombre: ")

print(nombre.lower())
print(nombre.upper())
print(nombre.title())