"""Programa que compara el mayor de 5 números solicitados al usuario y muestra el resultado por pantalla """

numero1 = int (input("Primer número: "))
numero2 = int (input("Segundo número: "))
numero3 = int (input("Tercer número: "))
numero4 = int (input("Cuarto número: "))
numero5 = int (input("Quinto número: "))

valores = [numero1, numero2, numero3, numero4, numero5] # Guardamos los números introducidos en un arraylist de números

mayor = numero1 # La variable 'mayor' actúa como variable de control

for i in range (5): # Recorremos con el bucle for el array y comparamos los valores de mayor con cada número

    if numero2 > mayor:
        
        mayor = numero2
        
    if numero3 > mayor:

        mayor = numero3
        
    
    if numero4 > mayor:

        mayor = numero4

    if numero5 > mayor:

        mayor = numero5

valores[i] +-1

print ("El número mayor es: ", mayor)

