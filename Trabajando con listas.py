
# Creamos una lista de 5 números

mi_lista = [1,2,3,4,5]

# Imprimimos por pantalla el contenido de la lista

print("La lista original contiene los siguientes números:", mi_lista)

# Asignamos al primer elemento de la lista [0], el valor 111

mi_lista[0] = 111

# Ahora la lista está modificada. Imprimos la lista modificada por pantalla

print("La lista modificada tiene ahora los siguientes valores: ", mi_lista)

# Ahora queremos copiar el valor del quinto elemento de la lista, al segundo

mi_lista[1] = mi_lista[4]

# De nuevo, volvemos a imprimir los valores de la lista modificada

print("Ahora la lista, tiene los siguientes valores: ", mi_lista)

# FUNCIÓN LEN() - Con esta función podemos ver la longitud de una lista. Veamos un ejemplo:

coleccion_numeros = [11, 22, 33, 44, 55, 66, 77, 88, 99]

print("El tamaño de la colección de números es: ", len(coleccion_numeros))

# Si queremos eliminar cualquier elemento de la lista, utilizaremos la INSTRUCCION del
# Para ello hay que apuntar a un elemento concreto de la lista

del coleccion_numeros[1]

print("Lista con el elemento [1] eliminado: ", coleccion_numeros)
print("Ahora la lista tiene la siguiente longitud:", len(coleccion_numeros))

# Si queremos añadir un nuevo elemento al final de la lista, utilizaremos el método append()

coleccion_numeros.append(100)

# Imprimimos la lista con el último elemento añadido 

print("La lista es ahora: ", coleccion_numeros)

# Ahora, si queremos insertar un nuevo elemento en cualquier lugar de la lista, utilizaremos el método insert(). Veamos un ejemplo de cómo funciona

coleccion_numeros.insert(1, 22)

coleccion_numeros.insert(8,99)

print(coleccion_numeros)

"""
Podemos iniciar la vida de una lista creándola vacía y luego agregar nuevos elementos según sea necesario.
Veamos un ejemplo utilizando un bucle for
"""

lista_blanca: list [int] = []

for i in range(10):
 lista_blanca.append(i + 1)

print("Esta es la lista blanca: ", lista_blanca)
 

lista_negra: list [int] = [] # La lista está vacía

for i in range(10): # Para todos los valores [i] de la lista hasta i-1
 lista_negra.insert (0, i + 1) # se inserta el elemento 0 y se incrementa el valor de i en una unidad hasta el final de la lista

print("Esta es la lista negra: ", lista_negra)

