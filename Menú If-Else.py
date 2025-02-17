""" Diseñar un programa que ofrezca un menú al usuario para calcular el diametro, el área o el perímetro de una circunferencia a partir de su radio """

from math import pi ## Importamos la función pi de la librería math
import string

radio = float(input("Por favor, introduce el valor del radio de la circunferencia:\n  "))

print ("------------------------ MENÚ ---------------------------")
print (" Opción 'a' - Calcular el diámetro de la circunferencia. ")
print (" Opción 'b' - Calcular el perímetro de la circunferencia. ")
print (" Opción 'c' - Calcular el área de la circunferencia. ")
print ("---------------------------------------------------------")

opcion = input("Por favor, teclea 'a', 'b' o 'c' según lo que desees calcular:\n ")

if opcion == 'a':

    diametro = 2 * radio
    
    print("El diámetro de la circunferencia es: ", diametro)

elif opcion == 'b':
    
    perimetro = 2 * pi * radio

    print ("El perímetro de la circunferencia es: ", perimetro)

elif opcion == 'c':
   
    area = pi * radio ** 2
    
    print ("El área de la circunferencia es: ", area)


elif opcion not in string.ascii_lowercase:
        print ("La opción seleccionada debe contener una letra en minúsculas y ningún caracter especial...")
        print(" | --Vuelve a ejecutar el programa -- |")
else:
     print("Introduce una letra válida de entre las proporcionadas en el menú, por favor. ")
        

