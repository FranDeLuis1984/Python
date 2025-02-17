
def mcd (n, m):
    while m%n != 0:
        mViejo = n
        nViejo = n

        m = nViejo
        n = mViejo%nViejo
    return n

class Fraction:

    def __init__(self, arriba, abajo): # Método constructor 
        
        self.num = arriba # El parámetro self es un parámetro especial que hace referencia al propio objeto
        self.den = abajo
    
    def __str__(self):
        return str (self.num) + "/" + str(self.den)  # El método _str_ convierte un objeto en este caso self, en una cadena de caracteteres
    
    def show (self):
        print (self.num), "/", (self.den)

    def _add_ (self, otraFraccion):

        nuevoNumero = self.num * otraFraccion.den + \
        self.den  * otraFraccion.num

        


        
    