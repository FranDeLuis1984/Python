""" Calcular la raíz n-ésima de un número leído por teclado, tomando valores entre 2 y 100."""

numero = int (input("Dame un número:  "))

for i in range (2, 101):
     
     resultado = numero ** (1/i)

     print(f"La raíz {i}-ésima de {numero} es {resultado:.2f}")