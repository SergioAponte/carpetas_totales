# By: Sergio Andrés Aponte Lamus 17/04/2024
""" 7.	Una panadería vende barras de pan a 3.49€ cada una. El pan que no es del día tiene un descuento del 60%.
Escribir un programa que comience leyendo el número de barras vendidas que no son del día. 
Después el programa debe mostrar el precio habitual de una barra de pan, 
el descuento que se le hace por no ser fresca y el coste final total. """

Barras_dia_no=int(input("Escriba el numero de barrar vendidas que no son de hoy: "))
print(f"El precio de una barra habitual es de: 3.49€ \n El descuento por no ser fresca es de {(Barras_dia_no*3.49)*0.6} \n El coste final es de: {(Barras_dia_no*3.49)-((Barras_dia_no*3.49)*0.6)}")
