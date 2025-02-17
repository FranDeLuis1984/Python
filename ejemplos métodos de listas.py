# Uso de los diferentes métodos para trabajar con listas

# Creación de la lista
mi_lista = [777, 3, True, 10.5] # Esta lista contiene varios elementos de los siguientes tipos: int, int, boolean, float

mi_lista.append (False) # Este método añade un nuevo item al final de la lista. Al pasarle el valor booleano 'False' como argumento, añade el valor False al final de la lista

print (mi_lista)

mi_lista.insert (2, 32) # El método insert añade el valor 32 en la posición 2 de la lista

print (mi_lista)

mi_lista.pop() # El método pop, elimina el ultimo item de la lista

# Ahora imprimimos el ultimo item 

print (mi_lista.pop())

# Creamos un nuevo objeto mi_lista2 con una secuencia de números ordenados de mayor a menor

mi_lista2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# El método sort ordena la lista en orden ascendente, de menor a mayor

mi_lista2.sort()

# Mostamos la lista llamando al método print

print(mi_lista2)

mi_lista2.reverse() # Con el método reverse(), modificamos la lista para que quede en orden inverso

# De nuevo, mostramos por pantalla la lista

print (mi_lista2)


print (mi_lista2.count(5)) # El método count(), devuelve el número de apariciones del item


