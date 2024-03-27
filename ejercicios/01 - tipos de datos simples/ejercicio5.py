#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el 
#coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

horas = float(input("Ingrese total de horas: "))
costo_hora = float(input("Ingrese el costo por hora: "))

print("el sueldo a cobrar es de: ", horas*costo_hora)
