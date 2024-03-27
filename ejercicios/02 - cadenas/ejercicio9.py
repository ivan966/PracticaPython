#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.

#fecha_nacimiento = input("Ingrese su fecha de nacimiento dd/mm/aaaa: ")
fecha_fija = "22/8/1996"
#print(f"Dia: {fecha_nacimiento[:2]}")
#print(f"Mes: {fecha_nacimiento[3:5]}")
#print(f"Año: {fecha_nacimiento[6:10]}")
dia = fecha_fija[:fecha_fija.find("/")]
mesanio = fecha_fija[fecha_fija.find("/")+1:]
mes = mesanio[:mesanio.find("/")]
anio = mesanio[mesanio.find("/")+1:]
print(f"Dia: {dia}")
print(f"Mes: {mes}")
print(f"Año: {anio}")