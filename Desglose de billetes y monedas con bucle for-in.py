"""
Realiza un programa en Pytthon que proporcione el desglose en billetes y monedas de una cantidad entera de euros. 
Recuerda que hay billetes de 500, 200, 100, 50, 20, 10 y 5€ y monedas de 2 y 1€. 
Debes «recorrer» los valores de billete y moneda disponibles con uno omás bucles for in.
"""

def desglose_euros(cantidad):


    # Creamos una lista de valores que almacena los billetes y las monedas

    valores = [500, 200, 100, 50, 20, 10, 2, 1]

    # Creamos un diccionario para efectuar el desglose

    desglose = {}

    # Recorremos cada valor dentro de la lista de valores 

    

    for valor in valores:
        if cantidad >= valor:
            # Calculamos cuantos billetes/monedas de este valor se necesitan
            cantidad_valor = cantidad // valor # División entera
            desglose[valor] = cantidad_valor
            # Actualizamos la cantidad restante 
            cantidad -= cantidad_valor * valor

     # Mostramos el desglose
    for valor, cantidad in desglose.items():
         if valor >= 5:
            print(f"{cantidad} billete(s) de {valor}€")
         else:
            print(f"{cantidad} moneda(s) de {valor}€")

cantidad = int(input("Introduce una cantidad entera de euros, por favor: "))
desglose_euros(cantidad)



