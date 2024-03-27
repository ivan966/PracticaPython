#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.


precio_pan = 3.49
descuento = 0.4
pan_vendido = int(input("ingrese cantida de barras de pan vendidas: "))
total = round(pan_vendido * precio_pan,2)
print(f"Total = {total}, descuento por pan de ayer = {round(total*descuento,2)}")