""" Ejercicio de iteración con bucle IF parte 2 """

Registro_nota = input("Introduce la nota que ha sacado el alumno en el examen:\n")

Nota = float (Registro_nota)

if Nota <5:
    print ("El alumno está suspenso")
else:
 if Nota == 5:
     print ("El alumno ha sacado un suficiente 'pelao'")
 else:
    if Nota <8:
     print ("El alumno ha sacado un bien")
    else:
       if Nota == 8 or Nota == 8.5:
          print ("El alumno es de notable")
       else:
          if Nota == 9 or Nota == 10:
             print ("¡Es un alumno de 10!")