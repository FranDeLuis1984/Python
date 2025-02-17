"""
Elaborar un algoritmo que permita ingresar el número de partidos ganados, perdidos y empatados, por ABC club en el torneo apertura, se debe de mostrar su puntaje total.
Consideraciones: Por cada partido ganado obtendrá 3 puntos, empatado 1 punto y perdido 0 puntos. 
"""
# DATOS DE ENTRADA

print ("Introduce el número de partidos ganados, por favor:")
partidos_ganados = int (input())
print ("Introduce el número de partidos empatados, por favor:")
partidos_empatados = int (input())
print ("Introduce el número de partidos perdidos, por favor:")
partidos_perdidos = int (input())

puntuacion_partidos_ganados = partidos_ganados * 3 # Cada partido ganado suma 3 ptos
puntuacion_partidos_perdidos = partidos_perdidos * 1 # Cada partido empatado acumula un punto 
puntuacion_partidos_empatados = partidos_empatados * 0 # Cada partido perdido se queda a 0 

puntuacion_total = int (puntuacion_partidos_ganados + puntuacion_partidos_empatados + puntuacion_partidos_perdidos) # calculamos la puntuación total , como la suma de partidos ganados, empatados y perdidos 

# DATOS DE SALIDA 

print ("La puntuación total es: ", puntuacion_total) # Mostramos por pantalla la puntuación total 
