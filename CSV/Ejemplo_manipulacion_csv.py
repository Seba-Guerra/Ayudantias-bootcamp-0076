import csv

"""
Maneras de manipular datos en archivos CSV con Python:

Leer y modificar fila por fila:

Leer: Recorres cada fila del archivo, modificas los datos que necesites y luego los vuelves a escribir en un nuevo archivo o en el mismo.
Ejemplo:

"""

with open('contactos.csv', 'r') as archivo_lectura, open('contactos_modificados.csv', 'w', newline='') as archivo_escritura:
    lector = csv.reader(archivo_lectura)
    escritor = csv.writer(archivo_escritura)

    for fila in lector:
        # Modificamos el segundo elemento de la fila (el teléfono)
        fila[1] = 'Nuevo número'
        escritor.writerow(fila)


"""
Utilizar un diccionario para cada fila:

Leer como diccionario: Con csv.DictReader, cada fila se convierte en un diccionario, lo que facilita el acceso a los datos por clave.
Ejemplo:

"""

with open('contactos.csv', 'r') as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        fila['telefono'] = 'Nuevo número'
        # ... otros cambios


"""
Operaciones comunes de manipulación:

1.-Agregar columnas: Crear nuevas columnas y asignarles valores.
2.-Eliminar columnas: Eliminar columnas que no sean necesarias.
3.-Filtrar filas: Seleccionar solo las filas que cumplan ciertas condiciones.
4.-Ordenar filas: Ordenar las filas según una columna específica.
5.-Agrupar datos: Agrupar filas según un criterio y realizar cálculos.
6.-Calcular estadísticas: Calcular la media, desviación estándar, etc. de los datos.
"""

# Ejemplo complejo: Agregar una columna calculada

with open('ventas.csv', 'r') as archivo_lectura, open('ventas_con_iva.csv', 'w', newline='') as archivo_escritura:
    lector = csv.reader(archivo_lectura)
    escritor = csv.writer(archivo_escritura)

    # Escribimos el encabezado con la nueva columna
    encabezado = next(lector) + ['IVA']
    escritor.writerow(encabezado)

    for fila in lector:
        precio = float(fila[1])
        iva = precio * 0.21  # Suponiendo un IVA del 21%
        fila.append(iva)
        escritor.writerow(fila)

"""

Consideraciones importantes:

Tipo de datos: Asegúrate de convertir los datos a los tipos adecuados (enteros, flotantes, etc.) antes de realizar cálculos.
Manejo de errores: Implementa mecanismos para manejar errores, como archivos no encontrados o datos incorrectos.
Eficiencia: Para grandes archivos, considera usar técnicas de lectura por bloques o bibliotecas como Pandas para mejorar el rendimiento.

"""
