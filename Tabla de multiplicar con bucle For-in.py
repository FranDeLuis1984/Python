""" Crear un programa que muestre la tabla de multiplicar de un número (5) introducido por el usuario """

# DATOS DE ENTRADA

numero = int(input("Dame un número: "))

# PROCESO Y SALIDA
for i in range(1, 11):  # Para mostrar la tabla del 1 al 10
    
    resultado = numero * i
    
    print(f"{numero} x {i} = {resultado}")