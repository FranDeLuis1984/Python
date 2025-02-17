## Se quiere calcular la distancia recorrida por un móvil (m) con velocidad constante (m/s) durante un tiempo t(sg)
## Considerar que el movimiento es MRU (movimiento recto uniforme)

# ENTRADAS DE DATOS

velocidad = input ("Por favor, introduce la veloidad a la que se desplaza el objeto móvil:\n")

tiempo = input ("Ahora introduce el tiempo:\n")

velocidad_movil = float(velocidad) # Realizamos un cast de String a Float
tiempo_movil = int(tiempo) # Realizamos un cast de String a Int

# Calculamos el espacio recorrido con la fórmula S = V * T y guardamos el resultado en una variable llamada espacio_recorrido

espacio_recorrido = velocidad_movil * tiempo_movil

# SALIDA DE DATOS

print (espacio_recorrido) # Mostramos por pantalla el valor de la variable 