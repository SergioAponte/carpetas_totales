# By: Sergio Andrés Aponte Lamus 17/04/2024
""" Un alumno desea saber cuál será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los siguientes porcentajes:
55% del promedio de sus tres calificaciones parciales.
30% de la calificación del examen final. 
15% de la calificación de un trabajo final. """

N1=float(input("Digite la primera Nota: "))
N2=float(input("Digite la segunda Nota:"))
N3=float(input("Digite la tercera Nota: "))
examen_final=float(input("Digite su examen final: "))
trabajo_final=float(input("Digite su trabajo final: "))
print(f"su calificacion final es {(((N1+N2+N3)/3)*0.55)+(examen_final*0.3)+(trabajo_final*0.15)}")