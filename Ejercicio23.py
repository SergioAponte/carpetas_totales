# By: Sergio Andrés Aponte Lamus 17/04/2024
""" 3.	Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y 
el número de años, y muestre por pantalla el capital obtenido en la inversión. """

inversion=int(input("Cantidad de dinero a invertir: "))
i_anual=float(input("Interes anual: "))
Num_años=float(input("Numero de años: "))
print(f"El capital obtenido es: {inversion*(1+i_anual**Num_años)}")

