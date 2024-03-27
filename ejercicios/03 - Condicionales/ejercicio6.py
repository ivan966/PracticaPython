#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

nombre = input("Ingrese su nombre: ")
genero = input("Ingrese su Sexo: ")

if genero[0].lower() == "f":
    if nombre[0].lower() <= "m":
        print("Grupo A")
    else:
        print("Grupo B")
else:
    if nombre[0].lower() >= "n":
        print("grupo A")
    else:
        print("grupo B")