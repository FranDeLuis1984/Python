""" EJERCICIO QUE EJEMPLIFICA EL USO DE FORMATOS DE CADENAS """

# Creamos e inicializamos las variables

Fruta = "Naranja"
Precio = 3

print ("La %s cuesta %d euros" % (Fruta, Precio))

Cesta_Fruta = { "Fruta" : "Plátano", "Precio" : 2}

print ("El %(Fruta)s cuesta %(Precio)d euros" %Cesta_Fruta)

