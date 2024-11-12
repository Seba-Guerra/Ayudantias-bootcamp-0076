from Vehiculos import Particular, Carga, Bicicleta, Motocicleta, Automovil, Vehiculo


nombres_clases = {
    Vehiculo: "Vehiculo",
    Automovil: "Automovil",
    Particular: "Particular",
    Carga: "Carga",
    Bicicleta: "Bicicleta",
    Motocicleta: "Motocicleta"
}


def guardar_datos_csv(vehiculos):
    try:
        with open('vehiculos.csv', 'w') as archivo:
            for vehiculo in vehiculos:
                datos = [str(type(vehiculo)), str(vehiculo.__dict__)]
                datos = ",".join(datos)
                archivo.write(datos + "\n")
        print("\nDatos guardados correctamente.")
    except Exception as error:
        print(f"Error al guardar los datos en el archivo: {str(error)}")


def leer_archivo_csv():
    vehiculos = {
        "Particular": [],
        "Carga": [],
        "Bicicleta": [],
        "Motocicleta": []
    }
    try:
        with open("vehiculos.csv", "r") as archivo:
            contenido = archivo.readlines()
            for linea in contenido:
                linea = linea.strip()
                clase, datos = linea.split(",{")
                datos = eval("{" + datos)
                clase = clase.replace(
                    "<class 'Vehiculos.", "").replace("'>", "")
                print(clase)
                clase = nombres_clases[eval(clase)]
                vehiculo = eval(clase)(**datos)
                vehiculos[clase].append(vehiculo.__dict__)
    except FileNotFoundError:
        print("El archivo vehiculos.csv no existe.")
    except Exception as error:
        print(f"Error al leer los datos del archivo {str(error)}")
    return vehiculos


# !("Toyota", "4Runner", 4, 120, 1500,5)<--Datos a ingresar: Marca, Modelo, Nro_Ruedas, Velocidad, Cilindraje, Puestos
particular = Particular("Toyota", "4Runner", 4, 120, 1500, 5)
# !("Toyota", "hilux", 4, 120, 1800,3000)<--Datos a ingresar: Marca, Modelo, Nro_Ruedas, Velocidad, Cilindraje, Capacidad de carga (kg)
carga = Carga("Toyota", "hilux", 4, 120, 1800, 3000)
# !("Bianchi", "Corsa", 2, "Mountain")<--Datos a ingresar: Marca, Modelo, Nro_Ruedas, tipo de bicicleta
bicicleta = Bicicleta("Bianchi", "Corsa", 2, "mountain")
# !("Ninja","300",2,"Deportiva","2T","Doble viga",21)<--Datos a ingresar: Marca, Modelo, Nro_Ruedas, Tipo, Cuadro, NRO Radios
motocicleta = Motocicleta(
    "Kawasaki", "ninja", 2, "Deportiva", "2T", "Doble viga", 21)

print("\nSus datos están siendo guardados en archivo vehiculos.csv...")
guardar_datos_csv([particular, carga, bicicleta, motocicleta])
print("\nSus datos fueron guardados correctamente")

print("\nLeyendo datos desde archivo vehiculos.csv...\n")
vehiculo_csv = leer_archivo_csv()
for clase, lista in vehiculo_csv.items():
    print(f"\nListado de vehiculos {clase}")
    for vehiculo in lista:
        print(vehiculo)
