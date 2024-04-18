# By: Sergio Andrés Aponte Lamus 17/04/2024
"""  Un alumno desea saber cuál será su promedio general en las tres materias más difíciles que cursa y cuál será el promedio que obtendrá en cada una de ellas. 
Estas materias se evalúan como se muestra a continuación: 
La calificación de Matemáticas se obtiene de la sig. manera:
Examen 90%
Promedio de tareas 10%
En esta materia se pidió un total de tres tareas.

La calificación de Física se obtiene de la sig. manera:
Examen 80%
Promedio de tareas 20%
En esta materia se pidió un total de dos tareas.

La calificación de Química se obtiene de la sig. manera:
Examen 85%
Promedio de tareas 15%
En esta materia se pidió un total de tres tareas. """

print("Promedio General de Matematicas\n")
n1_mate=float(input("Digite nota 1 matematicas: "))
n2_mate=float(input("Digite nota 2 matematicas: "))
n3_mate=float(input("Digite nota 3 matematicas: "))
Examen_final_mate=float(input("Digite nota examen: "))
porcentaje_notas_mate=((n1_mate+n2_mate+n3_mate)/3)*0.1
porcentaje_examen_mate=Examen_final_mate*0.9
Promedio_mate=round(porcentaje_notas_mate+porcentaje_examen_mate,2)
print(f"Su promedio en matematicas es: {Promedio_mate}\n")

print("Promedio General de Física\n")
n1_fisica=float(input("Digite nota 1 Física: "))
n2_fisica=float(input("Digite nota 2 Física: "))
Examen_final_fisica=float(input("Digite nota examen: "))
porcentaje_notas_fisica=((n1_fisica+n2_fisica)/2)*0.2
porcentaje_examen_fisica=Examen_final_fisica*0.8
Promedio_fisica=round(porcentaje_notas_fisica+porcentaje_examen_fisica,2)
print(f"Su promedio en física es: {Promedio_fisica}\n")

print("Promedio General de Química\n")
n1_quimica=float(input("Digite nota 1 Química: "))
n2_quimica=float(input("Digite nota 2 Química: "))
n3_quimica=float(input("Digite nota 3 Química: "))
Examen_final_quimica=float(input("Digite nota examen: "))
porcentaje_notas_quimica=((n1_quimica+n2_quimica+n3_quimica)/3)*0.15
porcentaje_examen_quimica=Examen_final_quimica*0.85
Promedio_quimica=round(porcentaje_notas_quimica+porcentaje_examen_quimica,2)
print(f"Su promedio en Química es: {Promedio_quimica}\n")

print("Promedio general en las 3 materias\n")
promedio_general=(Promedio_quimica+Promedio_fisica+Promedio_mate)/3
print(f"El promedio general es de: {promedio_general}")



