import math

### Diseñar un programa que permita operar con dos vectores y cree un menú para realizar operaciones ###

# Inicializamos la variable opción a la cadena vacia

opcion = ''
vector_1 = None
vector_2 = None

while opcion != '9':

    print (" ********* MENÚ DE OPERACIONES *********")
    print (" 1. - INTRODUCIR EL PRIMER VECTOR       ")
    print (" 2. - INTRODUCIR EL SEGUNDO VECTOR      ")
    print (" 3. - CÁLCULO DE LA SUMA DE VECTORES    ")
    print (" 4. - CÁLCULO DE LA DIFERENCIA DE VECTORES ")
    print (" 5. - CÁLCULO DEL PRODUCTO ESCALAR      ")
    print (" 6. - CÁLCULO DEL PRODUCTO VECTORIAL    ")
    print (" 7. - CÁLCULO DEL ÁNGULO ENTRE ELLOS    ")
    print (" 8. - CÁLCULO DE LA LONGITUD            ")
    print (" 9. - FINALIZAR PROGRAMA                ")
    print ("*****************************************")
    print()

    opcion = input ("Por favor, teclea un número de entre las opciones del menú para realizar las operaciones con vectores. Tecla '9' para finalizar el programa:\n ")

    if opcion == '1':

      try:

        # Solicitamos por teclado al usuario los valores de x1, y1, z1 del primer vector

        x1 = float (input ("Por favor, introduce el valor de x1: "))
        y1 = float (input("Por favor, introduce el valor de y1:  "))
        z1 = float (input("Por favor, introduce el valor de z1:  "))

        # Almacenamos la tripleta de valores en una lista llamada vector_1

        vector_1 = [x1, y1, z1]

        print ("El vector 1 se representa por los siguientes valores reales: ", vector_1)

      except ValueError:
         
         print ("Error. Debes ingresar valores numéricos. ")
    
    elif opcion == '2':
          
        try:
          
          # Solicitamos por teclado al usuario los valores de x2, y2 y z2 del segundo vector

          x2 = float (input("Por favor, introduce el valor de x2: "))
          y2 = float (input("Por favor, introduce el valor de y2: "))
          z2 = float (input("Por favor, introduce el valor de z2: "))

          # Almacenamos la tripleta de valores en una segunda lista llamada vector_2

          vector_2 = [x2, y2, z2]

          print ("El vector 2 se representa por los siguientes valores reales: ", vector_2)

        except ValueError:

            print ("Error. Debes ingresar valores numéricos. ")

    elif opcion == '3':
         
         if vector_1 is None or vector_2 is None:
              
              print ("Introduce los valores reales de cada vector, por favor. ")
         
         else:
              
              suma_vectores = [vector_1[i] + vector_2[i] for i in range(3)]
              
              print ("La suma de los vectores es: ", suma_vectores)
              print ()
    
    elif opcion == '4':
        
        if vector_1 is None or vector_2 is None:
              
              print ("Introduce los valores reales de cada vector, por favor. ")
         
        else:
              
              diferencia_vectores = [vector_1[i] - vector_2[i] for i in range(3)]
              
              print ("La diferencia de los vectores es: ", diferencia_vectores)
              print ()
            
    elif opcion == '5':

        if vector_1 is None or vector_2 is None:
              
              print ("Introduce los valores reales de cada vector, por favor. ")
         
        else:
              
              producto_escalar = sum (vector_1[i] * vector_2[i] for i in range (3))
              
              print ("El producto escalar de los vectores es: ", producto_escalar)
              print ()

    elif opcion == '6':
              
        if vector_1 is None or vector_2 is None:
              
              print ("Introduce los valores reales de cada vector, por favor. ")
         
        else:
              
              producto_vectorial = [
                  
                  vector_1[1] * vector_2[2] - vector_1[2] * vector_2[1], 
                  vector_1[2] * vector_2[0] - vector_1[0] * vector_2[2], 
                  vector_1[0] * vector_2[1] - vector_1[1] * vector_2[0] ]
              
              print ("El producto vectorial de los vectores es: ", producto_vectorial)
              print ()
    
    elif opcion == '7':
        
        
        if vector_1 is None or vector_2 is None:
            print("Debes introducir ambos vectores antes de calcular el ángulo.")
        else:
            
            producto_escalar = sum(vector_1[i] * vector_2[i] for i in range(3))
            norma_vector1 = math.sqrt(sum(vector_1[i] ** 2 for i in range(3)))
            norma_vector2 = math.sqrt(sum(vector_2[i] ** 2 for i in range(3)))
            
            if norma_vector1 == 0 or norma_vector2 == 0:
                
                print("No se puede calcular el ángulo con un vector nulo.")
            
            else:
                
                angulo_radianes = math.acos(producto_escalar / (norma_vector1 * norma_vector2))
                angulo_grados = math.degrees(angulo_radianes)
                print("El ángulo entre los vectores es:", angulo_grados, "grados")
                print ()

    elif opcion == '8':
        
        
        if vector_1 is None and vector_2 is None:
            
            print("Debes introducir al menos un vector antes de calcular la longitud.")
        
        else:
            
            if vector_1:
                
                longitud_vector1 = math.sqrt(sum(vector_1[i] ** 2 for i in range(3)))
                print("La longitud del primer vector es:", longitud_vector1)
                print()

            if vector_2:
                
                longitud_vector2 = math.sqrt(sum(vector_2[i] ** 2 for i in range(3)))
                print("La longitud del segundo vector es:", longitud_vector2)
                print()

    elif opcion == '9':

        print(" * Gracias por usar el programa * ¡Hasta luego! ")
        break

    else:

        print("Opción no válida. Por favor, selecciona una opción del menú.")
    



