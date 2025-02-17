import random # Importando la biblioteca random, podemos usar la función random.choice que selecciona un elemento aleatorio de una cadena o lista
import string # Importando la biblioteca string, tenemos acceso a string.ascii_lowercase que contiene todas las letras en minúsculas del alfabeto inglés


def generar_cadena ():
    
 Caracteres_Posibles = string.ascii_lowercase + " "  

# Creamos una variable Caracteres_Posibles que contiene todas las letras minúsculas y el espacio en blanco. Usamos string.ascii_lowercase para obtener 'abcdefghijklmnopqrstuvwxyz' y le sumamos el espacio ' ' para tener 27 caracteres posibles.

 Cadena_Generada = ''.join(random.choice(Caracteres_Posibles) for _ in range (27)) # Invocando al método join y la función random.choice selecciona dentro de un rango de 27 una cadena del abecedario y la almacena en el objeto Cadena_Generada
 
 return Cadena_Generada


def calificar_cadena (Cadena_Generada, Cadena_Objetivo):
 
# Declaración de variable local llamada contador de tipo int  inicializada a 0
 
 Contador = 0
  
 for i in range (len(Cadena_Objetivo)):  # El bucle For recorre cada elemento [i] de la cadena generada y la compara con la cadena objetivo 
 
  if Cadena_Generada [i] == Cadena_Objetivo [i]: # Si la comparativa de los caracteres de cada cadena coinciden, se incrementa el contador en 1
   Contador = Contador + 1

 return (Contador / len (Cadena_Objetivo)) * 100 

def mono_infinito (Cadena_Objetivo):
 
 # Inicialización de las variables
 Mejor_Cadena = None # Esta variable almacena la mejor cadena hasta el momento
 Mejor_Calificacion = 0.0 # Esta variable almacena la mejor calificación obtenida
 Intentos = 0 # Variable contador de intentos

 while True:
  Intentos += 1
 # Generamos una nueva cadena
  Cadena_Actual = generar_cadena()  # Cadena_Actual llama a la función generar_cadena () y almacena el valor de la cadena generada en Cadena_Actual
  # Calculamos su calificación actual 
  Calificacion_Actual = calificar_cadena (Cadena_Actual, Cadena_Objetivo)
  
  if Calificacion_Actual < Mejor_Calificacion:
    Mejor_Calificacion = Calificacion_Actual
    Mejor_Cadena = Cadena_Actual
  # Imprimimos el mejor resultado hasta el momento cada 1000 intentos
  if Intentos % 1000 == 0:
    print (f"Intentos: {Intentos}, "
    f"Mejor cadena hasta ahora: '{Mejor_Cadena}', "
                  f"Calificación: {Mejor_Calificacion:.2f}%")
        
  # Si la calificación actual es del 100%, hemos encontrado la secuencia correcta. 
  if Calificacion_Actual == 100.0:
            print(f"¡Cadena encontrada tras {Intentos} intentos!")
            print(f"Cadena correcta: '{Cadena_Actual}'")
            break






