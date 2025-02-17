from math import floor

# DATOS DE ENTRADA

grados = float(input("Dame un valor en grados:\n "))

cuadrante = floor(grados) % 360 // 90

if cuadrante == 0:
    
    print ("Primer cuadrante")

if cuadrante == 1:

    print ("segundo cuadrante")

if cuadrante == 2:

    print ("Tercer cuadrante")

if cuadrante == 3:

    print("cuarto cuadrante")

