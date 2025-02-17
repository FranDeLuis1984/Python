""" Programa que represente el porcentaje de suspensos, aprobados, notables y sobresalientes mediante el gráfico del pastel"""

from turtle import Screen, Turtle

# En primer lugar definimos el radio del circulo e inicializamos la variable

circulo = 300

# Inicializamos los porcentajes de las calificaciones como enteros de los suspensos, aprobados, notables y sobresalientes

suspensos = int (input("Introduce los suspensos: "))
aprobados = int (input ("Introduce los aprobados: "))
notables = int (input ("Introduce los notables: "))
sobresalientes = int (input ("Introduce los sobresalientes: "))


# Creamos un objeto pantalla como instancia de la clase Screen

pantalla = Screen()

# Creamos un objeto tortuga como instancia de la clase Turtle
tortuga = Turtle()

# Inicializamos la velocidad a la tortuga a 0

tortuga.speed (4)

# Empezamos a dibujar el radio

tortuga.penup()
tortuga.goto(0, - circulo)
tortuga.pendown()
tortuga.circle(circulo)
tortuga.penup()
tortuga.home() # Movemos la tortuga a sus coorrdenadas de origen (0, 0)
tortuga.pendown()

# Dibujo de la linea para los Supensos

angulo = (360 * suspensos / 100)
tortuga.left(angulo)
tortuga.forward(circulo)
tortuga.backward (circulo)

# Escribir el texto para los Suspensos

tortuga.penup()
tortuga.pensize(2)
tortuga.color ("red")
tortuga.right (angulo / 2)
tortuga.forward (circulo / 2)
tortuga.write (suspensos) 
tortuga.backward (circulo / 2)
tortuga.left(angulo / 2)
tortuga.pendown()

# Dibujo de la linea para los Aprobados

angulo = 360 * aprobados / 100
tortuga.left(angulo)
tortuga.forward(circulo)
tortuga.backward (circulo)

# Escribir el texto para los Aprobados

tortuga.penup()
tortuga.pensize (2)
tortuga.color ("blue")
tortuga.right (angulo / 2)
tortuga.forward (circulo / 2)
tortuga.write (aprobados)
tortuga.backward (circulo / 2)
tortuga.left(angulo / 2)
tortuga.pendown()

# Dibujo de la linea para los notables

angulo = 360 * notables / 100
tortuga.left(angulo)
tortuga.forward(circulo)
tortuga.backward (circulo)

# Escribir el texto para los Notables

tortuga.penup()
tortuga.pensize(2)
tortuga.color("Green")
tortuga.right (angulo / 2)
tortuga.forward (circulo / 2)
tortuga.write (notables)
tortuga.backward (circulo / 2)
tortuga.left(angulo / 2 )
tortuga.pendown()

# Dibujo de la linea para los Sobresalientes

angulo = 360 * sobresalientes / 100
tortuga.left(angulo)
tortuga.forward(circulo)
tortuga.backward (circulo)

# Escribir el texto para los Sobresalientes

tortuga.penup()
tortuga.pensize(2)
tortuga.color("Yellow")
tortuga.right (angulo / 2)
tortuga.forward (circulo / 2)
tortuga.write (sobresalientes)
tortuga.backward (circulo / 2)
tortuga.left(angulo / 2 )
tortuga.pendown()

tortuga.hideturtle()