# Sergio Aponte 16/04/2024

# 7.Escribir un programa que le pregunte al usuario por el numero de horas trabajadas y el coste por hora. Después debe 
# mostrar por pantalla la paga que le corresponde

print("Ingrese el numero de horas de trabajo")
horas=float(input())
print("Ingrese el coste por hora")
coste=int(input())
print(f"Su paga correspondiente es {horas*coste}")