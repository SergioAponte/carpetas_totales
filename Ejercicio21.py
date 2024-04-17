# By: Sergio Andrés Aponte Lamus 17/04/2024
""" 1.	Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo
del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas 
y otra solo con la primera letra del nombre y de los apellidos en mayúscula. """

Nombre_Completo=input("Digite su nombre completo: ")
print(f"{Nombre_Completo.lower()}\n{Nombre_Completo.upper()}\n{Nombre_Completo.title()}")