# En primer lugar se importan los módulos necesarios de la librería gráfica turtle, que son Screen y la clase Turtle
from turtle import Screen, Turtle

# A continuación, creamos un objeto pantalla a la que daremos un tamaño específico

pantalla = Screen()
pantalla.setup (600, 600)   # El método setup() da un tamaño y una posición a la pantalla creada en píxeles
pantalla.screensize (400, 200) # El método screensize fija el tamaño de la superficie del dibujo

tortuga = Turtle() # Creamos un objeto tortuga de la clase Turtle


for _ in range (3):
 
 tortuga.forward (100) # Avanza 100 pixeles
 tortuga.left (120) # Gira a la izquierda 120 grados

 
 
pantalla.mainloop()
