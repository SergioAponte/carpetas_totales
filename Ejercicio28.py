# By: Sergio Andrés Aponte Lamus 17/04/2024
""" Un maestro desea saber qué porcentaje de hombres y que porcentaje de mujeres hay en un grupo de estudiantes. """

hombre=int(input("Escribe el numero de hombres en el grupo: "))
mujeres=int(input("Escribe el numero de mujeres en el grupo: "))
print(f"El porcentaje de hombres es: {int((hombre/(hombre+mujeres))*100)}% \n El porcentaje de mujeres es de: {int((mujeres/(hombre+mujeres))*100)}%")