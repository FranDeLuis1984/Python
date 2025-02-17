### Como seguramente sabrás, debido a algunas razones astronómicas, el año pueden ser bisiesto o común. Los primeros tienen una duración de 366 días, mientras que los últimos tienen una duración de 365 días.

#Desde la introducción del calendario Gregoriano (en 1582), se utiliza la siguiente regla para determinar el tipo de año:

# Si el número del año no es divisible entre cuatro, es un año común.
# De lo contrario, si el número del año no es divisible entre 100, es un año bisiesto.
# De lo contrario, si el número del año no es divisible entre 400, es un año común.
# De lo contrario, es un año bisiesto.

año = int(input("Introduce un año: "))

if año < 1582:
    print("No dentro del período del calendario Gregoriano")
elif año % 4 != 0:
    print("Año Común")
elif año % 100 != 0:
    print("Año Bisiesto")
elif año % 400 != 0:
    print("Año Común")
else:
    print("Año Bisiesto")