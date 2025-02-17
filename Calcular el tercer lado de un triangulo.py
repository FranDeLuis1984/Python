import math # Importamos la librería para realizar el cálculo matemático

"""
Si se conoce la longitud de dos de los lados de un triángulo (b y c) y el ángulo entre ellos (alfa), expresado en grados sexagesimales, la longitud del tercer lado (a) se calcula por la fórmula:
a2 = b2 + c2-2bc*cos(alfa)
"""
print("------------------------------")
print(" CALCULAR EL TERCER LADO DE UN TRIANGULO ")
print("-------------------------------")

# Declaración de la constante PI

PI = 3.14165

# Datos de entrada

print("Introduce un lado del triangulo: ")
lado_b = float(input("Lado 'b' : "))
lado_c = float(input("Lado 'c' :  "))

print("Introduce ahora el ángulo del triángulo en grados sexagesimales: ")
alfa = float(input())

# Cálculo de la opereación

lado_a = ( lado_b**2 + lado_c**2 - 2*lado_b*lado_c * math.cos( alfa*PI/180 ) )**0.50

print("\nSALIDA")
print("------------")
print("El lado es: ", lado_a)

