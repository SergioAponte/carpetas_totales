# By: Sergio Andrés Aponte Lamus 17/04/2024
""" 2.	Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos 
ahorros debido a intereses, que no se cobran hasta finales de año,se te añaden al balance final de tu cuenta de ahorros.
Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. 
Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años.  """

ahorro=int(input("Cantidad de dinero a depositar: "))
primer_año=ahorro+(ahorro*0.04)
seg_año=primer_año+(primer_año*0.04)
ter_año=seg_año+(seg_año*0.04)
print(f"La cantidad de ahorros en los 3 años fue: \n Año 1: {primer_año} \n Año 2: {seg_año} \n Año 3: {ter_año}")