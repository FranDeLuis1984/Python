""" Dado el radio de un círculo, calcule el volumen de la esfera correspondiente."""

# Datos adicionales: El volumen de una esfera se calcula de la siguiente manera: V = 4/3 PI * r3

# DATOS DE ENTRADA

# Estbalecemos la constante PI, con su valor PI = 3.141516 

PI = 3.141516

# Solicitamos al usuario el radio del círculo y lo guardamos en una variable 

print ("Por favor, introduce el radio del círculo:")
radio = float (input("Radio: ")) # Realizamos un cast de String a Float

# Ahora calculamos el volumen de la esfera con los valores de PI y el radio

volumen_esfera = 4 / 3 * PI * radio ** 3

print ("\ SALIDA: ")
print ("------------------")
print ("El volumen de la esfera correspondiente es: ", volumen_esfera)

