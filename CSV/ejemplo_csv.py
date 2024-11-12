import csv
"""
Imagina que tienes una colección de juguetitos de tus personajes favoritos. Para tener un registro de quiénes son y qué características tienen.

En cada línea de tu cuaderno, escribes el nombre de la juguetito, su color, de qué película o serie es, separando cada dato con una coma. Al final, tienes una especie de tabla donde cada fila es una juguetito y
cada columna es una característica.

Un archivo .CSV (Comma Separated Values) es como ese cuaderno, pero en la computadora.

Comma Separated Values: Significa "Valores separados por comas".
Cada línea es una fila: Igual que en tu cuaderno, cada línea del archivo representa una juguetito (o un registro de información).
Cada columna es una característica: Cada columna representa una característica de la juguetito (nombre, color, etc.).

¿Por qué usamos archivos .CSV?:

Son fáciles de leer: Cualquier programa que pueda abrir un archivo de texto puede leer un archivo .CSV.
Son simples: No tienen una estructura muy compleja, lo que los hace fáciles de entender y modificar.
Son muy usados: Muchos programas y bases de datos pueden importar y exportar datos en formato .CSV.

"""

"""
La librería csv

Imagina que la librería csv es una caja de herramientas especial para trabajar con archivos CSV. Tiene varias herramientas para leer, escribir y manipular estos archivos.

Ejemplo:

Supongamos que tenemos un archivo CSV llamado "contactos.csv" con información de nuestros amigos. Cada línea del archivo tiene el nombre, el número de teléfono y el correo electrónico de un amigo, separados por comas.
"""


# Abrimos el archivo en modo lectura

with open('contactos.csv', 'r') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)

    # Iteramos sobre cada fila del archivo
    for fila in lector_csv:
        nombre, telefono, correo = fila
        print(f"Nombre: {nombre}, Teléfono: {telefono}, Correo: {correo}")

# Abrimos el archivo en modo escritura (sobreescribiendo el contenido existente)
with open('nuevos_contactos.csv', 'w', newline='') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)

    # Escribimos una nueva fila
    escritor_csv.writerow(
        ['Nuevo amigo', '123456789', 'nuevoamigo@ejemplo.com'])


"""
Explicación:

Importar la librería: (import csv) importa la librería csv para poder utilizar sus funciones.

Abrir el archivo: with open('contactos.csv', 'r') as archivo_csv: abre el archivo "contactos.csv" en modo lectura. El with asegura que el archivo se cierre correctamente al finalizar el bloque.

Crear un lector CSV: lector_csv = csv.reader(archivo_csv) crea un objeto lector que te permite iterar sobre las filas del archivo.

Leer las filas: El bucle for recorre cada fila del archivo. Cada fila es una lista con los valores separados por comas.

Escribir en un archivo: with open('nuevos_contactos.csv', 'w', newline='') as archivo_csv: abre un nuevo archivo "nuevos_contactos.csv" en modo escritura. El newline='' evita problemas con los saltos de línea.

Crear un escritor CSV: escritor_csv = csv.writer(archivo_csv) crea un objeto escritor para agregar nuevas filas al archivo.

Escribir una nueva fila: escritor_csv.writerow(['Nuevo amigo', '123456789', 'nuevoamigo@ejemplo.com']) escribe una nueva fila con los datos del nuevo amigo.
"""

"""

Características adicionales de la librería csv:
1.- Diferentes delimitadores: Puedes especificar un delimitador diferente al coma usando el argumento delimiter en csv.reader y csv.writer.
2.- Citar campos: Puedes encerrar campos con comillas usando el argumento quotechar.
3.- Leer y escribir diccionarios: Puedes leer y escribir datos en formato de diccionario usando csv.DictReader y csv.DictWriter.
"""
