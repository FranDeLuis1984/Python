"""Calculo de una ecuacion de segundo grado """
from math import sqrt

# DATOS DE ENTRADA

a = float (input("Escribe el valor de a: "))
b = float (input("Escribe el valor de b: "))
c = float (input(" Escribe el valor de c: "))

if a != 0:
    if b**2 - 4*a*c >= 0:
        x1 = (- b + sqrt(b**2 - 4*a*c)) / (2 * a)
        x2 = (- b - sqrt(b**2 - 4*a*c)) / (2 * a)
        print ("Las soluciones de x son:", x1, x2)
    else:
       print("No hay soluciones reales.")
else:
    if b != 0:
        x = - c / b
        print ("Solución: ", x)
    else:
        if c != 0:
            print ("La ecuación no tiene solución.")
        else:
            print ("La ecuación tiene infinitas soluciones. ")

        