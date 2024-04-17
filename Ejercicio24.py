# By: Sergio Andrés Aponte Lamus 17/04/2024
""" Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas, el vendedor desea saber cuánto dinero
 obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total 
que recibirá en el mes tomando en cuenta su sueldo base y comisiones. """

sueldo=int(input("Digite su sueldo: "))
v1=int(input("Escribe el valor de la primera venta: "))
v2=int(input("Escribe el valor de la segunda venta: "))
v3=int(input("Escribe el valor de la tercera venta: "))
comision=(v1+v2+v3)*0.1
print(f"Las comision del vendedor por las 3 ventas es de: {comision} \n Su sueldo final es de: {int(sueldo+comision)}")
