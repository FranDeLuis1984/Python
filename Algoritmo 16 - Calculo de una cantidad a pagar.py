""" Crear un algoritmo que Calcule el monto a pagar por un artículo si se tiene como datos de entrada la cantidad de docenas que compra y el costo por unidad de este artículo """

# NOTA: Al número de docenas “d” se multiplica por 12 para obtener el número de unidades del artículo y poder multiplicar por el precio unitario del artículo “c”.

# DATOS DE ENTRADA

print ("Introduce el número de docenas del artículo: ")
numero_docenas = float(input("Número de docenas: "))
print ("Introduce el coste por unidad del artículo: ")
coste_unidad = float(input("Coste unitario: "))

precio_total = numero_docenas * 12 * coste_unidad

print("\n SALIDA: ")
print("-------------------")
print(" Precio total a pagar:", precio_total, "€")
