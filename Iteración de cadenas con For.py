
""" Ejercicio de iteración de cadenas de texto con un bucle For """

# Creamos una primera lista de 3 Strings llamada Lista_Cadenas que contendra las cadenas: Gato, Perro y Conejo

Lista_Cadenas = ['Gato', 'Perro', 'Conejo']

# Creamos un objeto Lista vacío, llamado Lista_Letras, donde se irán guardando los caracteres de las palabras contenidas en Lista_Cadenas

Lista_Letras = []

for Una_Palabra in Lista_Cadenas:
   for Una_Letra in Una_Palabra:
       Lista_Letras.append(Una_Letra)
       print (Lista_Letras)

## El primer bucle for lee las letras de la Lista_Cadenas
## El sefundo bucle for añade cada letra de  Lista_Cadenas en el objeto Lista_Letras
## Finalmente se imprime por pantalla el objeto Lista_Letras