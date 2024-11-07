from Vehiculos import Automovil

# ! va a servir para a través de terminal capturar el dato requerido por el cliente
# * decimos que son 3
num_vehiculos = int(input("Cuantos vehiculos desea ingresar: "))
vehiculos = []  # ! para almacenar el número del input

for x in range(num_vehiculos):
    print("Datos del vehiculo", x + 1)
    marca = input("ingrese la marca del vehiculo: ")
    modelo = input("ingrese el modelo de su vehiculo: ")
    num_ruedas = input("ingrese el número de ruedas de su vehiculo: ")
    velocidad = input("ingrese la velocidad en KM/H: ")
    cilindraje = input("ingrese el cilindraje en CC: ")

    automovil = Automovil(marca, modelo, num_ruedas, velocidad, cilindraje)
    vehiculos.append(automovil)

print("Imprimiento por pantalla los vehiculos: ")
# ! Y = Variable de iteración | automovil = Variable de desplegado de información
for num_vehiculo, automovil in enumerate(vehiculos):
    print("Datos del automovil", num_vehiculo + 1, ":", "Marca", automovil.marca + "," "Modelo",
          automovil.modelo + "n", automovil.num_ruedas, "ruedas", automovil.velocidad, "KM/H,")
    print(automovil.cilindraje, "cc")

