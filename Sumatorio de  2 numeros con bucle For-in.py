""" Crear un programa que calcule el sumatorio de dos numeros m y n con un bucle for in range compacto """

n = int(input("Dame un número: "))
m = int(input("Dame otro número: "))

sumatorio = 0

for i in range (n, m + 1):

    sumatorio += i

    print(sumatorio)

    