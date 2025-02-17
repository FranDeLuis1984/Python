"""  Diseñar un programa que solicite tres valores al usuario (a, b y c) y calcule los valores de x para ña ecuación de segundo grado """
from math import sqrt

# DATOS DE ENTRADA

a = float (input("Escribe el valor de a: "))
b = float (input("Escribe el valor de b: "))
c = float (input(" Escribe el valor de c: "))

if a != 0:
    x1 = (- b + sqrt(b**2 - 4*a*c)) / (2 * a)
    x2 = (- b - sqrt(b**2 - 4*a*c)) / (2 * a)

    print ("Las soluciones de x son: ", x1, x2)
 
else:
    if a == 0:
        print ("No es una ecuación de segundo grado.")