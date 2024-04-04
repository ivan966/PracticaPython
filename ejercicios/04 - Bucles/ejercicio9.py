#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

user_pass = "password"
password = ""
while user_pass != password:
    password = input("Ingrese su Contraseña: ")
print("Bienvenido")