"""Diseñar un programa que lea la edad de dos personas y diga quién es más joven, la primera o la segunda. Ten en cuenta que ambas pueden tener la misma edad. En tal caso, hazlo saber con un mensaje adecuado. """

# DATOS DE ENTRADA

edad1 = int (input("La edad de Paco es:\n "))
edad2 = int (input("La edad de Manuel es:\n "))

if edad1 > edad2:
    
    print("Paco es mayor que manuel")

else:
    
    if edad1 < edad2:
        
        print ("Manuel es mayor que Paco")

    else:
      
      if edad1 == edad2:
        
        print ("Ambos tienen la misma edad")