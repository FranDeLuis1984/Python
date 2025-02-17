""" Máximo Cómun Divisor """

# Creamos la función y le pasamos dos números enteros por parámetro (n) y (m)

def mcd (m, n):
    while m%n != 0:
      
      mViejo = m
      nViejo = n

      m = nViejo
      n = mViejo%nViejo
      
    return n

print (mcd (20, 10))