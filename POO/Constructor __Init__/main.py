"""
Imagina que estás construyendo un castillo de arena. El constructor init es como una receta especial que te dice cómo construir las partes principales del castillo: las torres, el foso y el puente levadizo.

¿Por qué es importante?

Cuando creas un castillo nuevo, necesitas decidir de qué tamaño lo quieres, si quieres que tenga una bandera y qué color de arena usarás. El constructor init hace lo mismo con los programas: te permite decidir cómo quieres que sea
tu programa al principio, qué datos va a tener y cómo se va a comportar.

Un ejemplo sencillo:

Imagina que quieres crear un programa para un perro. El constructor init podría ser algo así:

"""


def __init__(self, nombre, raza, edad):
    self.nombre = nombre
    self.raza = raza
    self.edad = edad


"""
    nombre: El nombre que le pondrás a tu perro.
    raza: La raza del perro (labrador, pug, etc.).
    edad: La edad del perro.
"""


"""
Cuando creas un nuevo perro en tu programa, el constructor init se encargará de guardar toda esta información.

¿Por qué se llama init?

Es una palabra especial que significa "inicializar". Inicializar quiere decir "poner al principio". Así que el constructor init se encarga de poner al principio toda la información necesaria para que tu programa funcione correctamente.

En resumen:

El constructor init es como la receta que te dice cómo construir las partes principales de tu programa. Es muy importante porque te permite personalizar tu programa y darle las características que necesitas.

"""

"""
El constructor __init__ es una herramienta muy útil en la programación orientada a objetos de Python. Una vez que entiendes su función básica, puedes empezar a usarlo de muchas maneras.

¿Cómo utilizarlo?

Creando objetos:

Cuando creas un nuevo objeto de una clase, Python automáticamente llama al método __init__.
Los argumentos que le pases al constructor se utilizan para inicializar los atributos del objeto.

"""


class Perro:
    def __init__(self, nombre, raza, edad):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad


# Creando un nuevo objeto de la clase Perro
mi_perro = Perro("Firulais", "Labrador", 3)

"""
Inicializando atributos:

Dentro del método __init__, asignas valores a los atributos del objeto utilizando el self.
self hace referencia al objeto actual que se está creando.
Valores por defecto:

Puedes establecer valores por defecto para los atributos si no se proporcionan al crear el objeto.

"""

"""En este ejemplo, si no especificas la raza o la edad al crear un objeto, se utilizarán los valores por defecto."""


class Perro:
    def __init__(self, nombre, raza="Labrador", edad=2):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad


"""En este ejemplo, si no especificas la raza o la edad al crear un objeto, se utilizarán los valores por defecto."""


"""
Ejemplos de uso:

Creando objetos de diferentes tipos: Puedes crear clases para representar objetos del mundo real, como coches, personas, animales, etc. El constructor se encargará de inicializar los atributos específicos de cada objeto.

Validando datos: Puedes agregar lógica al constructor para validar los datos que se le pasan. Por ejemplo, puedes asegurarte de que la edad sea un número positivo o que el nombre no esté vacío.

Realizando cálculos iniciales: Puedes realizar cálculos simples dentro del constructor para inicializar ciertos atributos. Por ejemplo, si tienes una clase Círculo, puedes calcular el área del círculo en el constructor.
"""

"""
Un ejemplo más complejo:
"""

"""En este ejemplo, creamos una clase Auto con atributos como marca, modelo, año, color y kilometraje. El constructor inicializa estos atributos y proporciona valores por defecto para el color y el kilometraje."""


class Auto:
    def __init__(self, marca, modelo, año, color="rojo", kilometraje=0):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.kilometraje = kilometraje

    def arrancar(self):
        print("El auto está arrancando.")

    def acelerar(self):
        print("El auto está acelerando.")


"""En este ejemplo, creamos una clase Coche con atributos como marca, modelo, año, color y kilometraje. El constructor inicializa estos atributos y proporciona valores por defecto para el color y el kilometraje."""
