import math

numero = int (input("Escribe un número.... "))

if numero < 0:

    print("No se puede calcular el factorial de un número negativo. ")
else:
    print ("El factorial de", numero, "es", math.factorial(numero))

    