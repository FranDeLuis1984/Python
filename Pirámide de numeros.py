
# DATOS DE ENTRADA

valores = [0,1,2,3,4,5,6,7,8,9,10]

# PARTE CRECIENTE

for i in range(1, 11):            # i va desde 1 hasta 10
    for j in range(1, i + 1):     # j va desde 1 hasta i
        print(j, end=' ')
    print()                       # Salto de línea al terminar la fila

# Parte DECRECIENTE

for i in range(9, 0, -1):         # i va desde 9 hasta 1 (en decrecimiento)
    for j in range(1, i + 1):     # j va desde 1 hasta i
        print(j, end=' ')
    print()    