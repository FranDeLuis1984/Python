"""Elaborar un algoritmo que permita calcular el número de micro discos 3,5" necesarios para hacer una copia de seguridad, de la información almacenada en un disco cuya capacidad se conoce.
Hay que considerar que el disco duro está lleno de información, además expresado en gigabyte. Un micro disco tiene 1.44 megabyte y un gigabyte es igual a 1,024 megabyte.
"""
import math # Importamos la biblioteca math, para poder llamar a la función ceil() que redondea un número al entero superior

# El proceso de cálculo para determinar el número de Megabytes (MG) dado la cantidad de Gigabytes (GB) es MG = 1024 x GB, esto se puede determinar también si se aplica la regla de tres simple. 
# Para calcular el número de Micro discos de 3.5 se procede a dividir el número de Megabytes (MB) calculados entre 1.44 que es la capacidad de un solo Micro disco, así:
# MD = MG / 1.44


# DATOS DE ENTRADA

print ("Introduce el número de Gygabytes, por favor:")
gigabytes = float (input())

# PROCESO

megabytes = gigabytes * 1024
numero_discos = megabytes / 1.44

print("\n SALIDA:")
print("---------")
print (numero_discos)
print("---------")
print("El número de discos necersarios para realizar una copia de seguridad es:", math.ceil(numero_discos))

