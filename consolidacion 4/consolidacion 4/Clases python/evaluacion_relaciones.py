from Vehiculos import Particular, Carga, Bicicleta, Motocicleta, Automovil, Vehiculo


# ? for x in range(num_vehiculos):
# ?     print("\nDatos del vehiculo", x + 1)
# ?     marca = input("ingrese la marca del vehiculo: ")
# ?     modelo = input("ingrese el modelo de su vehiculo: ")
# ?     num_ruedas = input("ingrese el número de ruedas de su vehiculo: ")
# ?     velocidad = input("ingrese la velocidad en KM/H: ")
# ?     cilindraje = input("ingrese el cilindraje en CC: ")

# ?     automovil = Automovil(marca, modelo, num_ruedas, velocidad, cilindraje)
# ?     vehiculos.append(automovil)

# * Esto es un simil de imputs solicitados al usuario

# !("Toyota", "4Runner", 4, 120, 1500,5)<--Datos a ingresar: Marca, Modelo, Nro_Ruedas, Velocidad, Cilindraje, Puestos
particular = Particular("Toyota", "4Runner", 4, 120, 1500, 5)
# !("Toyota", "hilux", 4, 120, 1800,3000)<--Datos a ingresar: Marca, Modelo, Nro_Ruedas, Velocidad, Cilindraje, Capacidad de carga (kg)
carga = Carga("Toyota", "hilux", 4, 120, 1800, 3000)
# !("Bianchi", "Corsa", 2, "Mountain")<--Datos a ingresar: Marca, Modelo, Nro_Ruedas, tipo de bicicleta
bicicleta = Bicicleta("Bianchi", "Corsa", 2, "mountain")
# !("Ninja","300",2,"Deportiva","2T","Doble viga",21)<--Datos a ingresar: Marca, Modelo, Nro_Ruedas, Tipo, Cuadro, NRO Radios
motocicleta = Motocicleta(
    "Kawasaki", "ninja", 2, "Deportiva", "2T", "Doble viga", 21)

# * Esto es un simil de imputs solicitados al usuario

print("Vehiuculos listados: \n")

print(particular)
print(carga)
print(bicicleta)
print(motocicleta)

print("\nRelaciones de clases: \n")


#!isinstance Generamos comparación entre instanciamientos de clase

print(("Motocicleta es instancia con relación a Vehículo: "), isinstance(
    motocicleta, Vehiculo))
print("Motocicleta es instancia con relación a Automovil: ",
      isinstance(motocicleta, Automovil))
print("Motocicleta es instancia con relación a Vehículo particular: ",
      isinstance(motocicleta, Particular))
print("Motocicleta es instancia con relación a Vehículo de Carga: ",
      isinstance(motocicleta, Carga))
print("Motocicleta es instancia con relación a Bicicleta: ",
      isinstance(motocicleta, Bicicleta))
print("Motocicleta es instancia con relación a Motocicleta: ",
      isinstance(motocicleta, Motocicleta))
