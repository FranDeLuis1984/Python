# Mostrar el precio de IVA de un producto de 100€

# Declaración de variables
# IVA es una constante, su valor no cambia en todo el programa
IVA = 0.5
precio_producto = 100

# Calculamos el precio del IVA

precio_iva = precio_producto * IVA

# Imprimimos por pantalla el precio del IVA y el precio final con sus valores en €

print ("El precio del IVA es", precio_iva, "€")
print ("El precio final es", (precio_iva + precio_producto), "€")
