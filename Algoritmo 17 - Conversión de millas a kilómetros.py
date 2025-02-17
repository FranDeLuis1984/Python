""" Realizar un algoritmo que convierta millas a kilómetros
"""

print("--------------------------------")
print("-- CONVERSIÓN DE MILLAS A KMS --")
print ("-------------------------------")

# Declaración de constante

MI = 1.609344 # 1 Milla es equivalente a 1.609344 KM

# Datos de entrada

millas = float(input("Por favor, introduce el número de millas: ")) # Casting de String a Float

# Cálculo interno del proceso de conversión

kilometros = millas * MI # Esta es la fórmula de conversión de Millas a kilómetros

# Datos de salida

print("\nSALIDA: ")
print("----------")
print(millas, "Millas son:", kilometros, "Kilómetros")
