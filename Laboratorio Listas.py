"""
Había una vez un sombrero. El sombnrero no tenía conejo, sino una lista de 5 numeros 1, 2, 3, 4 y 5

Realizar:

1 - Una linea de código que solicite al usuario que reemplace el numero central en la lista con un numero
entero ingresado por el usuario
2 - Escribir una liunea de codigo que elimine el ultimo elemento de la lista
3 - Escribir una linea de codigo que imprima la longitud de la lista existente

"""

lista_sombrero = [1, 2, 3, 4, 5]

lista_sombrero[2] = int (input("Introduce un número entero: "))

del lista_sombrero[4]

print("La lista definitiva con el elemento central modificado es: ", lista_sombrero)
print("La longitud de la lista definitiva es: ", len(lista_sombrero))

