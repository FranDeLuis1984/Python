""" Calcular el area de un triangulo a partir de sus dos lados"""
import math

# DATOS DE ENTRADA

PI = 3.141516

lado1 = float (input("Dame el valor del lado 1 del triángulo:  "))
lado2 = float (input("Ahora dame el valor del lado 2 del triángulo: "))
angulo = float (input("Introduce también el valor del ángulo: "))

angulo_radianes = math.radians(angulo)

area_triangulo = 0.5 * lado1 * lado2 * math.sin(angulo_radianes)

print ("El área del triángulo es: ", area_triangulo)



