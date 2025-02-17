"""
Crear un algoritmo que calcule la distancia entre dos puntos (A y B) en el plano cartesiano
"""
# DATOS DE ENTRADA

print ("Ingresa las coordenadas del punto A, por favor:")

AX = float(input("AX: "))
AY = float(input("AY  "))

print ("Ahora, ingresa las coordenadas del punto B, por favor:")

BX = float (input("BX: "))
BY = float (input("BY: "))

distancia_total = ((AX-BX)**2 + (AY-BY)**2)**0.5

print("\n SALIDA:")
print("-------")
print("La distancia entre el punto A y el punto B es:", distancia_total)



