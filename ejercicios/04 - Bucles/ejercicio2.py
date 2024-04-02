#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

edad = int(input("Cual es tu edad? "))


for i in range(edad):
    print(f"edad: {i+1}")