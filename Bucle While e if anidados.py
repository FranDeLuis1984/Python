

while True:
      
      try: # Inicio de manejo de excepción

        numero = int (input("Introduce un número, por favor...")) # Solicitamos un número al usuario por teclado

    
        if numero < 0: # Si número introducido es menor que 0
            print("¡ADIOS!") # Se imprime por pantalla el mensaje: ¡ADIOS!
            break
        else:
            print ("Número introducido: ", numero) # Sino, se imprime por pantalla el número introducido

      except ValueError: # Cierre de manejo de excepción
          
          print ("Debes introducir un número válido")
           

       