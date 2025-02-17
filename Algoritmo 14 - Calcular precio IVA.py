""" Diseñar un algoritmo del IVA (21%), de un ordenador, dado el precio del mismo sin IVA"""
# DATOS DE ENTRADA

print("Introduce el precio del ordenador:")
precio_pc = float(input("Precio: "))

calculo_iva = precio_pc * 21 /100 # El cálculo del IVA se obtiene haciendo el 21% del precio del producto solicitado por el usario

print ("El IVA tiene un valor de: ", calculo_iva) # Imprimimos el resultado del IVA

precio_total = precio_pc + calculo_iva

print("El precio total de PC es: ", precio_total) # Imprimimos el precio total en otra variable separada1350


