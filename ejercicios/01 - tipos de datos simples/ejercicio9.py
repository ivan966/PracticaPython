#Escribir un programa que pregunte al usuario una cantidad a invertir, el
#interés anual y el número de años, y muestre por
#pantalla el capital obtenido en la inversión.

capital = float(input("ingrese el capital a invertir: "))
interes_anual = float(input("ingresar interes anual: "))
anios = int(input("ingrese cantidad de años a invertir: "))

interes = round(capital * (interes_anual/100 + 1)**anios,2)
#interes = (capital*(1+interes_anual)**anios)
print(interes)