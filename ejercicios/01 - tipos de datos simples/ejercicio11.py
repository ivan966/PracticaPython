#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de
# interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales
# de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa
# que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros,
# introducida por el usuario. Después el programa debe calcular y mostrar por
# pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear
# cada cantidad a dos decimales.

interes_anual = 4/100 + 1


dinero_depositado = float(input("ingrese dinero a depositar: "))

primer_anio = round(dinero_depositado * interes_anual,2)
segundo_anio = round(primer_anio * interes_anual,2)
tercer_anio = round(segundo_anio * interes_anual,2)

print(f"El primer año: {primer_anio} ")
print(f"El segundo año: {segundo_anio} ")
print(f"El tercer año: {tercer_anio} ")