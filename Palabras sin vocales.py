# Inicializar una cadena vacía para almacenar la palabra sin vocales
palabra_sin_vocales = ""

# Pedir al usuario que ingrese una palabra y convertirla a mayúsculas
palabra_usuario = input("Introduce una palabra: ").upper()

# Recorrer cada letra de la palabra
for letra in palabra_usuario:
    if letra not in "AEIOU":  # Si la letra no es una vocal, agregarla a la nueva palabra
        palabra_sin_vocales += letra  

# Imprimir la palabra sin vocales
print("Palabra sin vocales:", palabra_sin_vocales)