

# Diseña un programa que, dado un número entero, muestre por pantalla: "El número es par" cuando sea par y "El número es impar" cuando sea impar
# PISTA: Un número es impar cuando el resto de dividirlo por 2 es igual a 0, e impar en caso contrario

numero = int (input("Dame un número:\n "))

if numero % 2 == 0:
    print ("El numero es PAR. ")
else:
    if numero % 2 !=0:
        print ("El número es IMPAR. ")

