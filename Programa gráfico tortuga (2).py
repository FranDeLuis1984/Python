from turtle import Screen, Turtle


def dibujar_cuadrado_centrado (tortuga, lado, color_linea, color_relleno):

    # Dibuja un cuadrado con 'lado' tamaño, centrado en (0,0) con color_linea para el color del contorno y color_relleno para el relleno
  
  # Se calcula la mitad del lado para posicionarse en la esquina superior izquierda

  mitad = lado / 2


  tortuga.penup() # Levantamos el lápiz invocando al método penup()
  tortuga.goto(- mitad, mitad) # Invocando al método go-to() nos situamos en la esquina superior izquierda del cuadrado
  tortuga.pendown() # con el método pendown() volvemos a colocar el lapiz sobre la pantalla

  # Configuración de colores (contorno y relleno)

  tortuga.color (color_linea, color_relleno)

  # Comenzamos a rellenar el cuadrado. Para ello utilizamos un bucle for con rango 4 

  tortuga.begin_fill()
  
  for _ in range (4):
   
   tortuga.forward(lado)
   tortuga.right (90)

  tortuga.end_fill()

  # Configuración de la ventana 


pantalla = Screen()
pantalla.title("Dos cuadrados centrados: ")
pantalla.bgcolor("white")

tortuga = Turtle()
tortuga.speed ("slow")

dibujar_cuadrado_centrado (tortuga, 200, "red", "red")
dibujar_cuadrado_centrado (tortuga, 100, "blue", "blue")








