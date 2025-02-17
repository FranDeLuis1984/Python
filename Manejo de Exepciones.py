""" Ejercicio para el tratamiento de las excepciones en Python"""
import math


Dato = int (input("Por favor introduzca un numero:\n"))


print (math.sqrt(Dato))

try:
    print (math.sqrt(Dato))

except:
    print ("El valor de la raíz cuadrada es incorrecto. Se utilizará la función valor absoluto para tratar la excepción")
    print (math.sqrt(abs(Dato))) ## Muestra por pantalla la raíz del número, habíendolo convertido a valor absoluto invocando al método abs()
