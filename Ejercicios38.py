# By: Sergio Andrés Aponte Lamus 18/04/2024
"""39.	La presión, el volumen y la temperatura de una masa de aire se relacionan por la formula:
masa = (presión * volumen)/(0.37 * (temperatura + 460)) """

presion=float(input("Digite su presion: "))
volumen=float(input("Digite el volumen: "))
temperatura=float(input("Digite la temperatura: "))
masa=round((presion*volumen)/(0.37*(temperatura+460)),2)
print(f"La relacion de la masa de aire es de: {masa}")