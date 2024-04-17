cd_invertir=int(input("Escribe la cantidad a invertir: "))
int_anual=int(input("Escribe la tasa de interes anual: "))
num_años=int(input("Escribe la cantidad de años"))
print(f"El interes compuesto es {cd_invertir*((1+int_anual/100)**num_años)}")
