ingreso = float(input("Introduce el ingreso anual: "))

if ingreso <= 85.528:
 impuesto = (ingreso * 18 / 100) - 556.2
else:
    if ingreso > 85.258:
      impuesto = 14.839 + (ingreso - 85.528 * 32 / 100)

impuesto = round(impuesto, 0)
print("El impuesto es:", impuesto, "pesos")