""" CASO PRÁCTICO FINAL PYTHON - FRANCISCO DE LUIS MENÉ -"""

"""Programa en Python que gestiona libros y préstamos en una biblioteca. 
El programa debe incluye una clase Libro con métodos para agregar, prestar, devolver, mostrar y buscar libros. 
Se implementa un menú interactivo para que el usuario pueda realizar estas operaciones.
"""

# Creación de la lista para almacenar los libros

lista_libros =  [] # Se utiliza para almacenar los objetos de la clase Libro y para realizar operaciones como agregar, prestar, devolver y buscar libros

# Creación de la clase Libro

class Libro:

    # El método constructor (_init_), se ejecuta automáticamente cuando creamos una instancia (objeto), de la clase Libro.
    # Parámetros de _init_:
    #----------------------
    # SELF: Es una referencia de la instancia actual de la clase.
    # TITULO, AUTOR, ISBN son los valores que pasamos como argumentos al crear un nuevo objeto de la clase Libro


    def __init__(self, titulo, autor, isbn):
        
        self.titulo = titulo # Asigna el valor del parámetro título al atributo 'título'del objeto
        self.autor = autor # Asigna el valor del parámetro autor al atributo 'autor' del objeto
        self.isbn = isbn # Asigna el valor del parámetro isbn al atributo 'isbn del objeto
        self.disponible = True # Inicializa el atributo disponible a True, para indicar que un libro está disponible cuando se crea

    def agregar(self): # Este método añade el libro actual a la lista de libros
        
        lista_libros.append(self) # El método append() se utiliza para agregar un elemento a la lista
        print(f"El libro '{self.titulo}' se ha añadido correctamente.") # Se mnuestra un mensaje por pantalla diciendo que el libro se a añadido a la lista correctamente

    def prestar(self):

        if self.disponible:
            self.disponible = False
            print(f"El libro '{self.titulo}' se ha prestado con éxito.") # Si el libro está disponible, self.disponible == True, cambia su estado a False y muestra un mensaje de éxito.
        else:
            print(f"El libro '{self.titulo}' ya ha sido prestado, lo siento.") # Si el libro ya está prestado, muestra un mensaje indicando que no está disponible.
    
    def devolver(self):

        if not self.disponible:
            self.disponible = True
            print(f"El libro '{self.titulo}' se ha devuelto con éxito.") # Si el libro no está disponible (self.disponible == False), cambia su estado a True y muestra un mensaje de éxito.
        else:
            print(f"El libro '{self.titulo}' está disponible.") # Si el libro ya está disponible, muestra un mensaje indicando que no necesita ser devuelto.

    def mostrar(self):
        disponibilidad = "Sí" if self.disponible else "No"
        print(f"- {self.titulo} ({self.autor}) - ISBN: {self.isbn} - Disponible: {disponibilidad}") # Muestra los detalles del libro (título, autor, ISBN) y su estado de disponibilidad.

    @staticmethod
    def buscar(lista_libros, isbn): # Este método estático busca un libro en la lista biblioteca por su ISBN.
        for libro in lista_libros: # Bucle que recorre la lista en busca del libro
            if libro.isbn == isbn: # Si el libro se encuentra (búsqueda por atributo isbn como identificador único (ID) del libro)
                libro.mostrar() # Llamada al método mostrar() para mostrar sus detalles (TÍTULO, AUTOR, ISBN y DISPONIBILIDAD)
                return libro # se devuelve el objeto libro
        print(f"No se encontró ningún libro con el ISBN: {isbn}.") # Si no encuentra el libro, muestra un mensaje indicando que no se encontró.
        return None
    
#-----------------
# MENÚ INTERACTIVO
#-----------------
    
while True:
    print("\nBienvenido al Sistema de Gestión de Biblioteca")
    print("------------------------------------------------")
    print("1. Agregar libro")
    print("2. Prestar libro")
    print("3. Devolver libro")
    print("4. Mostrar libros")
    print("5. Buscar libro por ISBN")
    print("6. Salir")
    print("-------------------------------------------------")
    opcion = input("Elige una opción, por favor: ")

    if opcion == "1": # Solicita al usuario el título, autor e ISBN del libro.
        titulo = input("Título: ")
        autor = input("Autor: ")
        isbn = input("ISBN: ")
        nuevo_libro = Libro(titulo, autor, isbn) # Crea un nuevo objeto Libro con los argumentos añadidos por el usuario
        nuevo_libro.agregar() # y lo agrega a la lista de libros llamando al método agregar()

    elif opcion == "2":
        isbn = input("Introduce el ISBN del libro que se quiere prestar: ") # Solicita al usuario el ISBN del libro.
        libro = Libro.buscar(lista_libros, isbn) # Busca el libro en el listado de libros y si lo encuentra...
        if libro:
            libro.prestar() # Llama al método prestar() y si está disponible, lo presta

    elif opcion == "3":
        isbn = input("Introduce el ISBN del libro a devolver: ") # Solicita al usuario el ISBN del libro.
        libro = Libro.buscar(lista_libros, isbn) # De nuevo, como en la opción anterior, se llama al método buscar() de la clase libro que compara el ISBN introducido por el usuario con el ISBN del libro contenido en la lista.
        if libro: # Si el libro se encuentra en la lista
            libro.devolver() # LLama al método devolver() y lo devuelve

    elif opcion == "4":
        if not lista_libros: # Si no hay libros en la lista....
            print("¡Ooops! No hay libros en la biblioteca en estos momentos.") # Se muestra un mensaje diciendo que no hay libros en la biblioteca.
        else:
            print("\nLISTADO DE LIBROS:")
            print("--------------------")
            for libro in lista_libros:  # Si hay libros, se recorre cada objeto libro dentro de la lista.
                libro.mostrar() # Se llama al método mostrar() 

    elif opcion == "5":
        isbn = input("Introduce el ISBN del libro a buscar: ") # Se solicita al usuario que introduzca el ISBN del libro.
        Libro.buscar(lista_libros, isbn) # La sentencia Libro.buscar(lista_libros, isbn) llama al método estático buscar de la clase Libro, pasando dos argumentos.

    elif opcion == "6":
        print("Saliendo del programa...") # Muestra el mensaje saliendo del programa
        break # Sentencia que interrumpe el blucle while y sale del mismo.

    else:
        print("Opción inválida. ¡Inténtalo de nuevo!") # Si se introduce una opción incorrecta del menú, se muestra un mensaje de error y se vuelve a solicitar la opción
