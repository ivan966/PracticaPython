#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.


cantidad = float(input("Cantidad a invertir: "))
intereses = float(input("Interes Anual: "))
anios = int(input("Cantidad de Años: "))

for i in range(anios):
    cantidad *= (intereses / 100 + 1)
    print(f"Ganancias tras {i+1} años: {round(cantidad,2)}")