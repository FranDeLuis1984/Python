""" Calculamos una ecuación de primer grado con un bucle IF"""

# DATOS DE ENTRADA
# Solicitamos al usuario los valores a y b necesarios para resolver la ecuación de primer grado

a = float (input("¿Cual es el valor de a:\n "))
b = float (input("¿Cuál es el valor de b:\n "))

# La ecuación de primer grado, viene dada por la fórmula ax + b = 0. Por tanto el cálculo de x será x = -b / a



if a != 0:

    x = - b / a # Ecuación de primer grado

    print("La solución de la ecuación es: ", x)

if a == 0:
    
    if b != 0:
        
        print("La ecuación no tiene solución")
    
    if b == 0:

        print("La ecuación tiene multiples soluciones")

