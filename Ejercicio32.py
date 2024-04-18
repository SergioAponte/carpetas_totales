# By: Sergio Andrés Aponte Lamus 17/04/2024
""" En un hospital existen tres áreas: Ginecología, Pediatría, Traumatología. 
El presupuesto anual del hospital se reparte conforme a la sig. tabla:
    Área	     Porcentaje del presupuesto
    Ginecología	       40%
    Traumatología	   30%
    Pediatría	       30%
Obtener la cantidad de dinero que recibirá cada área, para cualquier monto presupuestal. """

presupuesto_anual=int(input("Digite el presupuesto anual: "))
Ginecologia=presupuesto_anual*0.4
Traumatologia=presupuesto_anual*0.3
Pediatria=presupuesto_anual*0.3
print(f"El presupuesto es de: {presupuesto_anual} y se reparte de esta forma: \n Ginecologia: {Ginecologia} \n Traumaotlogia:{Traumatologia} \n Pediatria: {Pediatria}")