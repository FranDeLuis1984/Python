""" Ejercicio de iteración con bucle IF"""
# Importación de la biblioteca math
import math

# Solicitamos al usuario un número entero que se gyuardará en la variable Dato de tipo String (cadena)

Dato = input ("Escribe un número entero, por favor\n")

Dato2 = int (Dato) ## Conversión explicita a tipo int (entero)

if Dato2 <0:
    print ("Lo siento, el número introducido es negativo")
else:
    print (math.sqrt(Dato2))
