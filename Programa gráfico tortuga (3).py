from turtle import Screen, Turtle

pantalla = Screen() # Creamos un objeto pantalla como instancia de la clase Screen
pantalla.setup (420, 225)
pantalla.screensize (400, 200)
pantalla.setworldcoordinates(-50, -150, 350, 250)

tortuga = Turtle() # Creamos un objeto tortuga como instancia de la clase Turtle

tortuga.pensize (3) # Da un grosor de 3 píxeles al trazo de la linea de la tortuga
tortuga.dot (10) # Dibuja un punto de diametro 10 en las coordenadas actuales
tortuga.forward (100)
tortuga.dot (10)
tortuga.forward (100)
tortuga.dot (10)
tortuga.forward (100)
tortuga.dot (10)

tortuga.penup()
tortuga.goto (0, 100) # Dirigimos a la tortuga a las coordenadas (0, 100)
tortuga.pendown()

tortuga.pencolor ("brown") # Damos el color marron a la tortuga
tortuga.pensize (5) # Ahora el grosor del trazo es de 5 píxeles
tortuga.circle(20) # Creamos un circulo de radio 20 
tortuga.forward (50)
tortuga.pensize(4) # Reducimos el grosor del trazo a 4 píxeles
tortuga.left (20)
tortuga.circle (20)
tortuga.forward (50)
tortuga.pensize(3) # Reducimos el grosor del trazo a 3 píxeles
tortuga.circle (20)
tortuga.forward (50)
tortuga.pensize(2) # Reducimos el grosor del trazo a 2 píxeles
tortuga.left (20)
tortuga.circle (20)
tortuga.forward (50)
tortuga.pensize(1)
tortuga.left (20)
tortuga.circle(20)
tortuga.forward (50)

tortuga.penup()

tortuga.goto (0, -100)
tortuga.write("Ey Honey")
tortuga.backward (20)
tortuga.write("Whats going on")

pantalla.mainloop()



