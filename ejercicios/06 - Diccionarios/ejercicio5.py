"""
Escribir un programa que almacene el diccionario con los créditos
de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5}
y después muestre por pantalla los créditos de cada asignatura en el formato
<asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las
asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar
también el número total de créditos del curso.
"""

asignaturas = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
total = 0
for asignatura, creditos in asignaturas.items():
    total += creditos
    print(f'la asignatura {asignatura} tiene {creditos} creditos')

print(f'el total de creditos del curso es {total}')