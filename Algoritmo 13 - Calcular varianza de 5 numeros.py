""" Algoritmo para calcular la varianza de cinco numeros"""

# DATOS DE ENTRADA

print ("Introduce 5 numeros por favor:")
numero1 = int (input("Numero 1: "))
numero2 = int (input("Numero 2: "))
numero3 = int (input("Numero 3: "))
numero4 = int (input("Numero 4: "))
numero5 = int (input("Numero 5: "))

sumatorio = numero1 + numero2 + numero3 + numero4 + numero5

# Para calcular la varianza, primero tenemos que calcular la media aritmética de los 5 números


media_aritmetica = numero1 + numero2 + numero3 + numero4 + numero5 / 5

# La formula de la varianza se calcula mediante la siguiente formula 

varianza = int (sumatorio - media_aritmetica) ** 2 / 5

print ("\n SALIDA: ")
print("----------------------")
print("La varianza de 5 numeros es: ", varianza)
