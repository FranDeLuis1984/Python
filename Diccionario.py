
""" Uso y aplicaciones de los diccionarios en Python """

# Creación de un diccionario

Capitales_España = {'Andalucia' : 'Sevilla', 'Aragón' : 'Zaragoza'}

# Mostramos por pantalla el elemento perteneciente a Andalucía (Sevilla)

print (Capitales_España ['Andalucia'])

# Añadimos un nuevo item a la estructura del diccionario

Capitales_España ['Asturias'] = 'Oviedo'

# Imprimimos la estructura modificada con el nuevo item

print (Capitales_España)

# Añadimos otro nuevo item a la coleccion del diccionario

Capitales_España ['Cantabria'] = 'Santander'

print (len(Capitales_España)) ## muesta por pantalla la longitud del diccionario

""" Uso del bucle for para recorrer el diccionario"""

# El bucle for recorre la estructura e imprime por pantalla cada una de las capitales 


for k in Capitales_España:

   print (Capitales_España [k], "es la capital de", k)





 


