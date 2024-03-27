#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

numero1 = int(input("ingrese primer numero: "))
numero2 = int(input("ingrese segundo numero: "))

if numero1 and numero2 != 0:
    if numero1 > numero2:
        print(numero1/numero2)
    else:
        print(numero2/numero1)
else:
    print("ERROR uno de los numeros ingresados es 0")