# Se leen tres números.
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
numero3 = int(input("Ingresa el tercer número: "))

# Verifica cuál de los números es el mayor
# y pásalo a la variable largest_number
    
numero_mayor = min(numero1, numero2, numero3)

# Imprime el resultado.
print("El número más grande es:", numero_mayor)