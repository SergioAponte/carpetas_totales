payasos=int(input("Escriba el numero de payasos vendidos: "))
muñecas=int(input("Escriba el numero de muñecas vendidos: "))
print(f"{int(((payasos*112+muñecas*75)/1000)*1500)}")