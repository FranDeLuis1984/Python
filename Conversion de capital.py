""" Crear un programa que pide al usuario una cantidad de euros, una tasa de interés y un número de años"""
""" Mostrar por pantalla, cuanto se habrá convertido el capital inicial transcurridos 'n' años, si cada año se aplica la tasa de interés introducida """

# DATOS DE ENTRADA

def conversion_capital():

  cantidad_euros = float (input("Escribe una cantidad en €: "))
  tasa_interes = float (input("¿Cuál es la tasa de interés anual? "))
  años = float (input("¿A cuantos años? :"))

  capital_convertido = cantidad_euros * (1 + tasa_interes / 100) ** años

  print("\n SALIDA: ")
  print("___________________")
  print("El capital convertido es: ", round(capital_convertido), "€")


conversion_capital()




