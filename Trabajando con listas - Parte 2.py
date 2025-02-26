
"""
Queremos calcular la suma de todos los valores almacenados en una lista
Utilizaremos una variable que almacenará la suma (total_suma) y que se inicializará a 0
Agregaremos todos los elementos de la lista usando el bucle FOR
"""

mi_lista = [10, 1, 8, 3, 5]
total_suma = 0

for i in range (len(mi_lista)):
    total_suma = total_suma + mi_lista[i]

print (total_suma)

"""
Ahora vamos a utilizar un bucle FOR para recorrer una lista, independientemente de la longitud
"""

longitud_lista = len(mi_lista) # Hemos asignado a la variable longtud_lista el valor de la longitud de nuestra lista

for i in range (longitud_lista // 2):
    mi_lista[i], mi_lista[longitud_lista - i - 1] = mi_lista[longitud_lista - i - 1], mi_lista[i]

print(mi_lista)
