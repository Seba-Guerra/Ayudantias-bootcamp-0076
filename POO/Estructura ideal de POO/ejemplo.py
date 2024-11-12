"""
Imagina que quieres construir una casa de muñecas. Tendrías diferentes piezas: paredes, techo, puertas, ventanas, muebles, etc. Cada pieza tiene sus propias características(tamaño, color, material) y funciones(abrir, cerrar, sostener).

En la programación orientada a objetos(POO), estas piezas son como las "clases". Una clase es como un molde que te permite crear muchos objetos iguales. Por ejemplo, podrías tener una clase llamada "Puerta" que defina las 
características de todas las puertas de tu casa de muñecas.

Los objetos son como las piezas individuales que creas a partir del molde. Podrías crear muchas puertas diferentes usando la clase "Puerta", pero cada una tendría sus propias características específicas(color, tamaño).

¿Por qué es útil la POO?

Organización: Al separar el código en clases y objetos, tu programa se vuelve más fácil de entender y mantener.
Reutilización: Puedes reutilizar las mismas clases para crear diferentes programas. Por ejemplo, la clase "Puerta" podría utilizarse en cualquier programa que necesite una puerta.
Extensibilidad: Puedes crear nuevas clases que hereden las características de clases existentes, lo que te permite agregar nuevas funcionalidades a tu programa de forma sencilla.
¿Cómo elegir la mejor estructura POO?

No hay una respuesta única a esta pregunta, ya que la mejor estructura dependerá del problema que estés tratando de resolver. Sin embargo, aquí te dejo algunos consejos:

Identifica los objetos: Piensa en los elementos principales de tu programa y trata de identificar las clases que los representan.
Define los atributos: ¿Qué características tienen estos objetos? Estos serán los atributos de tus clases.
Define los métodos: ¿Qué acciones pueden realizar estos objetos? Estos serán los métodos de tus clases.
Relaciona las clases: ¿Cómo se relacionan las diferentes clases entre sí? Puedes usar relaciones como herencia, composición o agregación.
"""

"""Ejemplo de uso de POO:"""


"""En este ejemplo, "Perro" es una clase. "mi_perro" es un objeto creado a partir de la clase "Perro". El objeto "mi_perro" tiene los atributos "nombre" y "raza", y puede realizar la acción "ladrar"."""


class Perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    def ladrar(self):
        print("¡Guau!")


mi_perro = Perro("Fido", "Labrador")
mi_perro.ladrar()

"""En este ejemplo, "Perro" es una clase. "mi_perro" es un objeto creado a partir de la clase "Perro". El objeto "mi_perro" tiene los atributos "nombre" y "raza", y puede realizar la acción "ladrar"."""


"""Metodos para abordar un problema y solucionarlo desde la perspectiva de POO"""

"""
Divide y vencerás:

Identifica los objetos: Busca los elementos clave de tu problema y trata de representarlos como objetos.
Define las clases: Crea clases para cada tipo de objeto, incluyendo sus atributos y métodos.
Establece relaciones: Define cómo se relacionan las clases entre sí (herencia, composición, agregación).
Abstracción:

Foca en lo esencial: No te preocupes por los detalles de implementación al principio. Concéntrate en la lógica general de tu programa.
Oculta la complejidad: Utiliza métodos para encapsular la lógica interna de tus objetos y hacer que su uso sea más sencillo.
Reutilización:

Identifica código común: Busca secciones de código que se repitan y encapsúlalas en funciones o métodos.
Utiliza bibliotecas: Aprovecha las bibliotecas existentes para realizar tareas comunes.
Pruebas:

Escribe pruebas unitarias: Asegúrate de que cada parte de tu código funcione correctamente de forma independiente.
Depura tu código: Utiliza herramientas de depuración para encontrar y corregir errores.
Diseño:

Sigue principios de diseño: Considera principios como SOLID (Single Responsibility, Open-Closed, Liskov Substitution, Interface Segregation, Dependency Inversion) para crear un código más mantenible y escalable.
Utiliza diagramas: Crea diagramas de clases para visualizar la estructura de tu programa.

"""
