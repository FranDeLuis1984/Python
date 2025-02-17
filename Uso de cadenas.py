# Uso y funcionalidad de las cadenas

# Creación de variable

nombre = "Francisco"
apellido = "de Luis"

# Mostramos por pantalla los items 2 y 0 de las variables nombre y apellido respectivamente

print (nombre[2]) 
print (apellido[0])

# El método len() nos devuelve la longitud de la cadena e invocando a la funcion print nos mostrará por pantalla dicha longitud


print (len(nombre))

"""
Ahora vamos a trabajar con métodos útiles para cadenas y secuencias

"""
# Creamos e inicializamos una nueva variable

mi_nombre = "Paquito"

# Vamos a hacer una invocación al método Upper() para convertir todas las letras en mayúsculas y lo mostraremos por pantalla

print (mi_nombre.upper())

# Con el uso del método find (()) Se devuelve el índice de la aparición del primer item 

print (mi_nombre.find('q'))

# La invocación al método center(), devuelve una cadena centrada en un campo de tamaño 'x'

print (mi_nombre.center(5))

# El método split(), trunca la cadena desde un caracter

print (mi_nombre.split('u'))
