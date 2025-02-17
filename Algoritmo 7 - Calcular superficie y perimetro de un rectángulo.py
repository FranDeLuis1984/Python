"""
Crear un algoritmo tal que, dado como datos la base y la altura de un rectángulo, calcule el perímetro y la superficie de este.
"""
# DATOS DE ENTRADA

# Solictamos al usuario los datos de base y altura, casteamos ambos valores a tipo de punto flotante (float) y guardamos los valores en sus respectivas variables

print ("Introduce la base y la altura del perímetro del rectángulo, por favor:")
base = float (input("Base:  "))
altura = float (input("Altura: "))

# CÁLCULO DE LA SUPERFICIE Y EL PERÍMETRO DEL RECTÁNGULO

superficie = base * altura
perimetro = 2 * (base + altura)

# DATOS DE SALIDA

print ("La superficie (área) del rectángulo es:", superficie)
print ("El perimetro del rectángulo es:", perimetro)
