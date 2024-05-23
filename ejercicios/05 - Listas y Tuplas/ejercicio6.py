"""
Escribir un programa que almacene las asignaturas de un curso
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista,
pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la
lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla
las asignaturas que el usuario tiene que repetir.
"""
asignaturas = ["Matematicas","Fisica","Quimica","Historia","Lengua"]
aprobadas = []

for asignatura in asignaturas:
    nota = int(input(f"ingrese nota de la materia {asignatura}\n"))
    if nota >= 5:
        aprobadas.append(asignatura)

for asignatura in aprobadas:
    asignaturas.remove(asignatura)

print(f"las materias que tienes que repetir son {asignaturas}")

