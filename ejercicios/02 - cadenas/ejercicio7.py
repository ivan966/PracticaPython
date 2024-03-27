#Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.

correo = input("ingrese su correo: ")
# el correo.find toma toda la cadena hasta el @ que esta entre los parentesis del find luego concatena la cadena que tomo con lo que se le agrego despues.
print(correo[:correo.find('@')]+ "@ceu.es")