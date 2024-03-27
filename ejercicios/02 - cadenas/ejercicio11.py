#Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.

nombre_producto = input("Ingresar nombre de producto: ")
precio_producto = float(input("Ingrese precio: "))
cantidad_producto = int(input("Cantidad: "))

print(f"producto: {nombre_producto} \n precio: {round(precio_producto,2)} \n Unidades: {round(3,cantidad_producto)} \n Total: {precio_producto*cantidad_producto}")