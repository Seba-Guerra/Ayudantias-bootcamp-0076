"""Imagina que tienes una caja de juguetes muy especial. En lugar de guardar los juguetes todos revueltos, tú decides poner cada juguete en un cajón diferente. En la puerta de cada cajón, pegas una etiqueta con el nombre del juguete.

Esa caja de juguetes es como un diccionario. Los juguetes son las palabras y los cajones son las definiciones. Cuando quieres saber qué significa una palabra, buscas la etiqueta con esa palabra y abres el cajón para ver su definición.

Por ejemplo:

Juguete: autito de juguete
Cajón (definición): Vehículo de cuatro ruedas que se usa para transportar personas.
En Python, los diccionarios funcionan de manera similar:

En lugar de juguetes, tenemos "claves". Estas claves pueden ser palabras, números o cualquier otra cosa.
En lugar de cajones, tenemos "valores". Los valores son la información asociada a cada clave."""

"""Ejemplo en Python:"""

mi_diccionario = {"manzana": "fruta roja", "perro": "animal doméstico"}

"""manzana" es la clave.
"fruta roja" es el valor asociado a la clave "manzana".
¿Por qué son útiles los diccionarios?

Organizan la información: Al igual que tu caja de juguetes, los diccionarios te ayudan a mantener tus datos ordenados y fáciles de encontrar.
Son muy flexibles: Puedes guardar cualquier tipo de información en un diccionario, desde números hasta listas o incluso otros diccionarios."""

"""¿Quieres ver un ejemplo más complejo?

Imagina que quieres guardar la información de tus amigos. Podrías crear un diccionario donde cada clave sea el nombre de tu amigo y el valor sea otro diccionario con más información, como su edad, su color favorito y su 
animal favorito."""


amigos = {
    "Ana": {"edad": 10, "color": "azul", "animal": "gato"},
    "Pedro": {"edad": 8, "color": "rojo", "animal": "perro"}
}


"""Los diccionarios son herramientas muy versátiles en Python y tienen un montón de usos. Aquí te explico algunas formas en las que puedes utilizarlos:

1. Almacenar información relacionada:

Datos personales: Puedes crear un diccionario para guardar el nombre, la edad, la ciudad y otros detalles de una persona.
Inventarios: Puedes almacenar información sobre productos en un inventario, como el nombre del producto, el precio y la cantidad en stock.
Configuraciones: Puedes guardar las configuraciones de una aplicación en un diccionario, como el idioma, el tema y otras opciones.
2. Crear estructuras de datos más complejas:

Diccionarios anidados: Puedes crear diccionarios dentro de otros diccionarios para representar estructuras de datos más complejas, como árboles genealógicos o estructuras de datos de juegos.
Listas de diccionarios: Puedes crear listas donde cada elemento sea un diccionario, para representar una colección de objetos con las mismas propiedades.
3. Acceder a información de forma rápida:

Buscar valores por clave: Puedes acceder rápidamente al valor asociado a una clave específica.
Iterar sobre los elementos: Puedes recorrer todos los pares clave-valor de un diccionario utilizando un bucle for.


Ejemplo práctico:
Imagina que quieres crear un diccionario para guardar la información de un libro:"""

libro = {
    "titulo": "El señor de los anillos",
    "autor": "J.R.R. Tolkien",
    "genero": "Fantasía",
    "paginas": 1178
}

print("El título del libro es:", libro["titulo"])
print("El autor es:", libro["autor"])

"""Otras operaciones comunes con diccionarios:"""

# Agregar nuevos elementos: libro["editorial"] = "Minotauro"
# Modificar valores existentes: libro["paginas"] = 1200
# Eliminar elementos: del libro["genero"]
# Verificar si una clave existe: if "autor" in libro:
# Obtener todas las claves: claves = libro.keys()
# Obtener todos los valores: valores = libro.values()
