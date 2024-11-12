"""Imagina que tienes una caja de juguetes. En esa caja puedes guardar tus carritos, tus muñecos, tus bloques y todos tus juguetes favoritos, ¿verdad?

Una lista en programación es como esa caja, pero para guardar cosas dentro de una computadora. En vez de juguetes, podemos guardar números, palabras, o incluso otras listas más pequeñas.

Por ejemplo: Imagina que quieres hacer una lista de tus frutas favoritas. Podrías escribir:

* Manzana
* Banana
* Uva
* Naranja
En programación, escribiríamos esto así:"""

frutas = ["manzana", "banana", "uva", "naranja"]

"""¿Para qué sirven las listas?

Las listas son muy útiles porque nos permiten organizar información de una manera fácil. Por ejemplo, podemos usar listas para:

Hacer la compra: Crear una lista con todos los alimentos que necesitamos comprar.
Guardar los nombres de tus amigos: Hacer una lista con los nombres de todos tus amigos.
Almacenar los resultados de un juego: Guardar los puntajes de todos los jugadores.
¡Y muchas cosas más! Las listas son una herramienta fundamental en la programación, y son muy fáciles de usar.

¿Te gustaría aprender más sobre las listas? Podemos hablar de cómo agregar cosas a una lista, cómo quitar cosas, o cómo buscar cosas dentro de una lista. ¡Tú me dices!"""

# "Casos de uso:"

"""Para hacer una compra: """

compra = ["leche", "pan", "huevos", "frutas"]

"""Para guardar puntajes de un juego:"""

puntajes = [100, 80, 95, 70]

"""Para crear un menú:"""

menu = ["pizza", "pasta", "ensalada", "hamburguesa"]

"""Para almacenar usuarios:"""

usuarios = ["Ana", "Juan", "Pedro", "Maria"]

"""Para añadir elementos a una lista:"""

frutas.append("pera")  # Agrega "pera" al final de la lista

"""Para quitar elementos de una lista:"""

frutas.remove("banana")  # Quita "banana" de la lista

"""Para acceder a un elemento en una lista:"""

print(frutas[0])  # Imprime el primer elemento de la lista (manzana)

"""Para recorrer una lista:"""

for fruta in frutas:
    print(fruta)  # Imprime cada fruta en una línea diferente

"""Para ordenar una lista:"""

frutas.sort()  # Ordena la lista alfabéticamente
