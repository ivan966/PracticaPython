"""
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
"""

tipo_pizza = int(input("Elija que pizza desea \n1: Pizza vegetariana \n2: Pizza no vegetariana\n"))
if tipo_pizza == 1:
    ingredientes = input("Ingredientes disponibles, elija uno: \n 1: Pimenton \n 2: Tofu\n")
    print(f"su pizza contiene los siguientes ingredientes: \n mozzarella \n tomate \n {ingredientes}")
else:
    ingredientes = input("Ingredientes disponibles, elija uno: \n 1: Peperoni \n 2: Jamon \n 3: Salmon\n")
    print(f"su pizza contiene los siguientes ingredientes: \n mozzarella \n tomate \n {ingredientes}")