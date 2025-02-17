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

class Fraccion: # CLASE FRACCION
   
   # Definimos el método constructor

   def __init__(self, arriba, abajo): # El método constructur _init_ consta de tres parámetros. 1 de ellos es self un parametro especial que hace referencia al objeto
      
      self.num = arriba
      self.den = abajo

   def __str__(self): # El método _str_ devuelve un objeto convertido a cadena
      return str(self.num) + "/" + str(self.den)

   def mostrar(self): # El método mostrar imprime los valores llamados por el parametro especial self
      print (self.num, "/", self.den)
    
    
   
   def __add__(self,otraFraccion): 
         
         nuevoNum = self.num*otraFraccion.den + \
            self.den*otraFraccion.num
         nuevoDen = self.den * otraFraccion.den
         comun = mcd(nuevoNum,nuevoDen)
         return Fraccion(nuevoNum//comun,nuevoDen//comun)

   
   def __eq__(self, otro):
         primerNum = self.num * otro.den
         segundoNum = otro.num * self.den

         return primerNum == segundoNum
   
x = Fraccion(1,2)
y = Fraccion(2,3)
print(x+y)
print(x == y)