import math

x = - 1

while x < 0:
    
 try:

    x = float (input("Introduce un numero positivo. "))
    
    if x < 0:
        print ("El número debe ser positivo, inténtalo de nuevo...")

 except ValueError:
      print ("Entrada nó válida, debes ingresar un número. ")
      x = -1

print (f"La raíz cuadrada de {x} es: {math.sqrt(x)}")