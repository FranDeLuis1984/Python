# Obtener el promedio simple de un estudiante a partir de sus tres notas parciales N1, N2 y N3.

# ENTRADA DE DATOS

nota1 = int (input("nota 1:  ")) # Cast de String a int. Esta variable guarda el valor de la nota 1
nota2 = int (input("nota 2:  ")) # Cast de String a int Variable nota 2 de tipo entero
nota3 = int (input("nota 3:  ")) # Cast de String a int

# El promedio se calcula según la siguiente formula P = (N1 + N2 + N3) / 3

promedio = int(( nota1 + nota2 + nota3) / 3) # calculamos el promedio y lo guardamos en su variable correspondiente 

# DATOS DE SALIDA

print("El promedio de las 3 notas es:", promedio)
