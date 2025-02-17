""" Escribir un algoritmo que calcule el perimetro de un triángulo equilátero """

# Datos adicionales: La fórmula para calcular el perímetro de un triangulo equilatero es p = 3a (sienda a la altura)

# DATOS DE ENTRADA

print ("Escribe la altura del triángulo: ")
altura = float (input ("Altura:  ")) # Cast de tipo string a tipo float

perimetro = 3 * (2* altura) / 3**0.5 # Fórmula que calcula el perímetro de un triángulo equilátero

print ("El perimetro del triangulo es: ", perimetro) 

