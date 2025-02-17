from math import pi
import string

""" Diseñar un programa que ofrezca un menú al usuario para calcular el diametro, el área o el perímetro de una circunferencia a partir de su radio """
""" El usuario debe poder tener una opción para finalizar el programa """

# Solicitamos el radio al usuario por teclado

radio = float (input("Introduce el radio de la circunferencia, por favor... "))

opcion = ''

while opcion != 'd':

    print ("--------------   MENÚ  ------------------")
    print (" 1. Opción 'a' - DIÁMETRO                ")
    print (" 2. Opción 'b' - ÁREA                    ")
    print (" 3. Opción 'c' - PERÍMETRO               ")
    print (" 4. Opción 'd' - FINALIZAR PROGRAMA      ")
    print ("-----------------------------------------")

    opcion = input("Por favor, teclea 'a', 'b', 'c' o 'd' para iniciar o finalizar el programa: ")

    if opcion == 'a':
        
        diametro = 2 * radio 
        print ("El diámetro de la circunferencia es: ", diametro)
    
    elif opcion == 'b':
        perimetro = 2 * pi * radio
        print  ("El perímetro de la circunferencia es: ", perimetro)
    
    elif opcion == 'c':

        area = pi * radio ** 2
        print ("El área de la circunferencia es: ", area)

    elif opcion == 'd':
        print ("Sólo hay 4 opciones 'a', 'b', 'c' o 'd'. Tu has tecleado: ", opcion)

    elif opcion not in string.ascii_letters:
        print (" --- La opción seleccionada no puede contener caracteres especiales ----") 
    
    elif opcion.isupper():
        print (" --- La letra introducida tiene que ser en minúsculas ----")

print ("¡¡ Gracias por utilizar el programa !!")
