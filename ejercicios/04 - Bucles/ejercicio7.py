#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

for i in range(1,11):
    for a in range(11):
        print(f"{i*a}", end="\t")
    print("")