"""Crear un programa que muestre todos los multiplos de 6 entre 6 y 150 ambos inclusive """

# INICIALIZACIÓN DE VARIABLES

valor_inicial = 6
limite = 150

for i in range (6, limite +1):
  
  if i % valor_inicial == 0:
   print(i)

