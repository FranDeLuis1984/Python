""" Escribir un algoritmo que, dada una cantidad de soles, proporcione su equivalente en dólares y después en euros. Se sabe que 1 dólar =3.25 soles y 1 euro=3.83 soles.
"""
# Declaramos las constantes que van a ejecutarse durante el programa

EURO = 3.84
DOLAR = 2.28

print("Introduce una cantidad de soles, por favor: ")
soles = float (input("Soles: "))

dolares = soles / DOLAR
euros = soles / EURO

print ("\n SALIDA:   ")
print("-------------------")
print("La cantidad de soles", soles, "en dolares es: ", dolares)
print("La cantidad de soles", soles, "en euros es: ", euros) 
