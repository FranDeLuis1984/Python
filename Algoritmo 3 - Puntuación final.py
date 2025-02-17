# Crear un algoritmo que solicite el número de respuestas correctas, incorrectas y en blanco, correspondientes a postulantes, y muestre su puntuación final
# considerando que por cada respuesta correcta tendrá 3 puntos, respuestas incorrectas tendrá -1 y respuestas en blanco tendrá 0.

"""
Para establecer el proceso de cálculo atenderemos a lo siguiente:

Cálculo de Puntuación de respuestas correctas (PRC) = RC * 3
Cálculo de Puntuación de respuestas incorrectas (PRI) = RC * -1
Cálculo de Puntuación de respuestas en blanco (PRB) = RC * 0

Puntuación final = PRC + PRI + PRB

"""

# DATOS DE ENTRADA

print ("Escribe el número de respuestas correctas, por favor:")
respuestas_correctas = int (input()) # Cast a tipo entero y se guarda el valor en la variable respuestas_correctas
print ("Escribe el número de respuestas incorrectas, por favor:")
respuestas_incorrectas = int(input()) # Cast a tipo entero y se guarda el valor en la variable respuestas_incorrectas
print ("Escrible el número de respuestas en blanco, por favor:")
respuestas_en_blanco = int(input()) # Cast a tipo entero y se guarda el valor en la variable respuestas en blanco

puntuacion_respuestas_correctas = respuestas_correctas * 3
puntuacion_respuestas_incorrectas = respuestas_incorrectas * -1
puntuacion_respuestas_en_blanco = respuestas_en_blanco * 0

puntuacion_final = int (puntuacion_respuestas_correctas + puntuacion_respuestas_incorrectas + puntuacion_respuestas_en_blanco)

print ("La puntuación final es:", puntuacion_final)

