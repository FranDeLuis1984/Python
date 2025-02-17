""" Programa que compara el mayor de tres números introducidos por pantalla"""

numero_1 = int (input("Primer número: "))
numero_2 = int (input("Segundo número: "))
numero_3 = int (input("Tercer número: "))
numero_4 = int (input("Cuarto número: "))
numero_5 = int (input("Quinto número: "))


# Variable para almacenar el mayor; inicialmente es el primer número
mayor = numero_1

# Comparamos con el segundo
if numero_2 > mayor:
    
    mayor = numero_2

# Comparamos con el tercero
if numero_3 > mayor:
    
    mayor = numero_3

# Comparamos con el cuarto
if numero_4 > mayor:
    
    mayor = numero_4

# Comparamos con el quinto
if numero_5 > mayor:
    
    mayor = numero_5

print("El número mayor es:", mayor)


