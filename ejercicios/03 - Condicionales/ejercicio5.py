#Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

edad = int(input("ingrese su edad: "))
ingresos = float(input("cuanto es su ingreso: "))

if(edad >= 16):
    if(ingresos >= 1000):
        print("Debe tributar")
    else:
        print("No debe tributar")
else:
    print("No debe tributar")