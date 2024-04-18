# By: Sergio Andrés Aponte Lamus 17/04/2024
""" Tres personas deciden invertir su dinero para fundar una empresa. Cada una de ellas invierte una cantidad distinta. 
Obtener el porcentaje que cada uno invierte con respecto a la cantidad total invertida. """
inversor1=int(input("Digite primera cantidad invertida: "))
inversor2=int(input("Digite segunda cantidad a invertir: "))
inversor3=int(input("Digite tercera cantidad a invertir: "))
cantidad_total=inversor1+inversor2+inversor3
porcentaje_inv_1=round((inversor1/cantidad_total)*100,2)
porcentaje_inv_2=round((inversor2/cantidad_total)*100,2)
porcentaje_inv_3=round((inversor3/cantidad_total)*100,2)
print(f"El porcentaje del inversor 1 es: {porcentaje_inv_1}%\n El porcentaje del inversor 2 es: {porcentaje_inv_2}% \n El porcentaje del inversor 3 es: {porcentaje_inv_3}% ")
