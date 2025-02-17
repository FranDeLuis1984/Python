"""
En este ejercicio se trabajará con los conjuntos y sus métodos
"""

# Creación de los conjuntos

conjunto1 = {'ave', 'perro', 'gato', 'ratón'}
conjunto2 = {'peto', 'kiwi', 'rayo'}

## -- MÉTODO UNION() -- ##
# Devuelve un nuevo conjunto con todos los elementos de ambos conjuntos

print (conjunto1.union(conjunto2))

## -- Operador |  -- ##
# El operador | Devuelve un nuevo conjunto con todos los elementos de ambos conjuntos

print (conjunto1 | conjunto2)

## -- Método intersection () -- ## Devuelve un nuevo conjunto con sólo los elementos comunes a ambos conjuntos

print (conjunto1.intersection(conjunto2))

## -- Método add() Añade un item a un conjunto

conjunto2.add('perez')

## -- Método issubset() pregunta si todos los elementos de un conjunto están en el otro

print (conjunto1.issubset(conjunto2))

