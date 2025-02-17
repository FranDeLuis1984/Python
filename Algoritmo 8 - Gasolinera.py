"""
Construir un algoritmo que resuelva un problema que tiene una gasolinera. Los dispensadores de esta registran loque “surten” en galones, pero el precio de la gasolina está fijadoen litros. 
El algoritmo debe calcular e imprimir lo que hay que cobrarle al cliente.
"""

# CREACIÓN DE CONSTANTES

# Las constantes mantienen el valor durante todo el programa

LITROS_GALON = 3.785
PRECIO_LITRO = 4.50

print ("¿Cuantos litros de gasolina se han consumido?:")
consumo = float(input()) # Cast de un tipo String a un tipo float

total_consumido = consumo * LITROS_GALON * PRECIO_LITRO # Cálculo del total consumido (para su calculo multiplicaremos el consumo por cada una de las constantes declaradas a nivel global)

# Como las constantes mantienen el valor, su valor permanece en el cálculo 

# DATOS DE SALIDA

print ("Se han consumido un total de: ", total_consumido) # Se imprime por pantalla el total consumido 
