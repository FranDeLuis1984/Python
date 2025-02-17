""" Realiza un programa que calcule el desglose mínimo en billetes y monedas de una cantidad exacta de euros. Hay billetes de 500, 200, 100, 50, 20, 10 y 5 € """

# DATOS DE ENTRADA

cantidad = float (input ("Dame una cantidad en €, por favor: "))

desglose1 = cantidad // 500
desglose2 = cantidad // 200
desglose3 = cantidad // 100
desglose4 = cantidad // 50
desglose5 = cantidad // 20
desglose6 = cantidad // 10
desglose7 = cantidad // 5

if desglose1 == 1:
    print("1 billete de 500€ y 2 de 200€ ")
if desglose2 == 3:
    print ("3 billetes de 200€ y 1 billete de 100€ ")
if desglose3 == 7:
    print ("7 billetes de 100€ y 1 billete de 50€ ")
if desglose4 == 15:
    print("15 billetes de 50€ y 1 billete de 10€ ")
if desglose5 == 38:
    print ("38 billetes de 20€ ")
if desglose6 == 76:
    print ("76 billetes de 10€")
if desglose7 == 152:
    print ("152 billetes de 5€")

