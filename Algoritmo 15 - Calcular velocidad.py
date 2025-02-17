""" Dados el tiempo y la distancia recorrida de un móvil, calcular a partir de estos datos, la velocidad del mismo"""

# DATOS DE ENTRADA

print ("Introduce el tiempo y la distancia del móvil: ")
tiempo = float (input("Tiempo: "))
distancia = float (input("Distancia:  "))

# Para calcular la velocidad del móvil, lo haremos a traves de la siguiente fórmula: velocidad = distancia / tiempo

velocidad = distancia / tiempo

# DATOS DE SALIDA

print("\n SALIDA: ")
print ("--------------------")
print ("La velocidad del movil es: ", velocidad, "m/s")

