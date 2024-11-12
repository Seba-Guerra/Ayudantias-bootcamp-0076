"""      
Explicación:

Clase Libro: Definimos una clase llamada Libro para representar un libro.

Constructor __init__: El constructor toma como parámetros el título, autor, año y un valor booleano disponible por defecto a True (indicando que el libro está disponible).
"""
"""
Métodos:
prestar(): Cambia el estado del libro a no disponible si está disponible y muestra un mensaje.
devolver(): Cambia el estado del libro a disponible si no está disponible y muestra un mensaje.
Creación de objetos: Creamos tres objetos de la clase Libro para representar diferentes libros.
Uso de los métodos: Llamamos a los métodos prestar() y devolver() para simular el préstamo y la devolución de libros.
"""
"""
¿Qué hace este código?
Organiza la información: Cada libro se representa como un objeto con sus propios atributos (título, autor, año, disponibilidad).
Simula acciones: Los métodos prestar() y devolver() simulan las acciones que se pueden realizar con un libro.
Facilita la gestión: Podemos crear muchos objetos de tipo Libro y realizar operaciones sobre ellos de manera sencilla.
"""

"""
¿Qué más podemos hacer?
Agregar más atributos: Podríamos agregar atributos como el género del libro, la editorial, etc.
Crear métodos adicionales: Podríamos crear métodos para buscar libros por título, autor o año.
Implementar una biblioteca: Podríamos crear una clase Biblioteca para gestionar una colección de libros y permitir realizar operaciones como agregar libros, buscar libros disponibles, etc.
"""


class Libro:
    def __init__(self, titulo, autor, año, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.disponible = disponible

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"Lo sentimos, el libro '{self.titulo}' no está disponible.")

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            print(f"El libro '{self.titulo}' ha sido devuelto.")
        else:
            print(f"El libro '{self.titulo}' ya está disponible.")


# Crear varios libros
libro1 = Libro("El señor de los anillos", "J.R.R. Tolkien", 1954)
libro2 = Libro("1984", "George Orwell", 1949)
libro3 = Libro("Orgullo y prejuicio", "Jane Austen",
               1813, False)  # Este libro ya está prestado

# Prestar un libro
libro1.prestar()

# Devolver un libro
libro3.devolver()
