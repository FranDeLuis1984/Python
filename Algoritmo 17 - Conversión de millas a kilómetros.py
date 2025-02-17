""" Realizar un algoritmo que convierta millas a kilómetros
"""

print("--------------------------------")
print("-- CONVERSIÓN DE MILLAS A KMS --")
print ("-------------------------------")

# Declaración de constante

MI = 1.609344 # 1 milla es equivalente a 1.609344 km

# Datos de entrada

millas = float(input("Por favor, introduce el número de millas: "))

# Cálculo interno del proceso de conversión

kilometros = millas * MI

# Datos de salida

print("\nSALIDA: ")
print("----------")
print(millas, "millas son:", kilometros, "kilómetros")
