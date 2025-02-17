# Un programa que lee una secuencia de números
# y cuenta cuántos números son pares y cuántos son impares.
# El programa termina cuando se ingresa un cero.

numeros_impares = 0
numeros_pares = 0

# Lee el primer número.
numero = int(input("Introduce un número o escribe 0 para detener: "))

# 0 termina la ejecución.
while numero != 0:
    # Verificar si el número es impar.
    if numero % 2 == 1:
        # Incrementar el contador de números impares.
        numeros_impares += 1
    else:
        # Incrementar el contador de números pares.
        numeros_pares += 1
    # Leer el siguiente número.
    numero = int(input("Introduce un número o escribe 0 para detener: "))

# Imprimir resultados.
print("Cuenta de números impares:", numeros_impares)
print("Cuenta de números pares:", numeros_pares)