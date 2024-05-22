"""
Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
"""
palabra = ""
while True:
    palabra = str(input("Ingrese una palabra: "))
    if palabra == "salir":
        print("finalizando el programa")
        break
    print(palabra)

