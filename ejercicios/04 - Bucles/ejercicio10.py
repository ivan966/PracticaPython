#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

numero = int(input("Ingrese un numero: "))
cont = 0;
for i in range(1,numero+1):
    if numero%i == 0:
        cont += 1
        print(f"contador: {cont}")

if cont == 2:
    print("primo")
else:
    print("natural")