""" Crear un programa que solicite al usuario el nombre y lo muestre mil veces por pantalla"""

def repetir_nombre_mil_veces(): # definicion de funcion

    nombre = input("Introduce un nombre, por favor: ") # Solicitud de nombre

    print ((nombre + " ") * 1000)

repetir_nombre_mil_veces() # Llamada a la función
