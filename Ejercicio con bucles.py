"""Diseña un programa que solicite la lectura de un texto que no contenga letras mayúsculas. Si el usuario teclea una letra mayúscula, el programa solicitará nuevamente la introducción del texto cuantas veces sea preciso."""

while True:

    texto = input("Por favor introduce una cadena de texto....")

    if texto.islower():
        print("El texto introducido es: ", texto)
        break
    else:
     print ("El texto solo debe contener letras minúsculas, por favor, inténtalo de nuevo. ")



