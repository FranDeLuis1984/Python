""" Construya un algoritmo tal que, dado como datos el radio y la altura de un cilindro, calcule e imprima el área y su volumen. """

# DATOS DE ENTRADA

# Declaramos la constante PI que mantendrá su valor durante toda la ejecución de un programa

PI = 3.141516

print ("Introduce el radio y la altura del cilindro, por favor:")

radio = float (input("Radio: "))
altura = float (input("Altura: "))

# Para calcular el volumen de un cilindro, se realiza mediante la siguiente fórmula matemática = V= πr2h

volumen = PI * radio ** 2 * altura

# Para calcular el área de un cilindro, se realizará la siguiente fórmula matemática: A total =2πr2 +2πrh

area_total = 2 * PI * radio ** 2 + 2 * PI * radio * altura

# DATOS DE SALIDA

print ("\n SALIDA:  ")
print ("------------ ")
print ("El volumen de un cilindro es: ", volumen)
print ("El área de un cilindro es: ", area_total)
