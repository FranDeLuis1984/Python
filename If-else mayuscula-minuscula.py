import string

caracter = input("Escribe una letra mayuscula o minuscula: ")

if caracter in string.ascii_lowercase:
    print("La letra introducida es minúscula.")
elif caracter in string.ascii_uppercase:
    print("La letra introducida es mayúscula.")
else:
    print("El carácter introducido no es una letra.")

   
    
