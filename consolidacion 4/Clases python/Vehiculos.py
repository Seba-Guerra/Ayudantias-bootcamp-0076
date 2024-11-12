
#!clase padre
class Vehiculo:
    def __init__(self, marca, modelo, num_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.num_ruedas = num_ruedas

    # ? atributo adicional de formato string especifico en el cual me entregará: Marca x | Modelo y | xy ruedas
    def __str__(self):  # ? Hey soy un texto = __str__ que se considere como atributo
        # almacenando información
        return f"Marca: {self.marca}, Modelo: {self.modelo}, ruedas: {self.num_ruedas}"

#!clase padre

#! clase hijo


class Automovil(Vehiculo):
    def __init__(self, marca, modelo, num_ruedas, velocidad, cilindraje):
        # ! Hay una relación entre Padre (Vehiculos) hacia Hijo (Automovil)
        # ? Atributos Generales (Padre)
        super().__init__(marca, modelo, num_ruedas)
        # ? Atributos particulares (Hijo)
        self.velocidad = velocidad
        self.cilindraje = cilindraje


#! clase hijo

# considerando la información almacenada
# almacenando información velocidad

#! clase nieto de Automovil


class Particular(Automovil):
    # ! Hay una relación entre Padre (Automovil) hacia Hijo (Particular)
    def __init__(self, marca, modelo, num_ruedas, velocidad, cilindraje, puestos):
        super().__init__(marca, modelo, num_ruedas, velocidad, cilindraje)
        self.puestos = puestos

    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, ruedas: {self.num_ruedas}, velocidad: {self.velocidad}, cilindraje:, {self.cilindraje}, puestos: {self.puestos})"


#! clase nieto de automovil


#! clase nieto de Automovil
class Carga(Automovil):
    def __init__(self, marca, modelo, num_ruedas, velocidad, cilindraje, peso_carga):
        super().__init__(marca, modelo, num_ruedas, velocidad, cilindraje)
        self.peso_carga = peso_carga

    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, ruedas: {self.num_ruedas}, velocidad: {self.velocidad}, cilindraje: {self.cilindraje},capacidad de carga (KG): {self.peso_carga}"

#! clase nieto de automovil

#! clase nieto de Vehiculo


class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, num_ruedas, tipo):
        super().__init__(marca, modelo, num_ruedas)
        self.tipo = tipo

    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, ruedas: {self.num_ruedas}, tipo de bicicleta: {self.tipo}"

#! clase bisnieto de Vehiculo


class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, num_ruedas, tipo, motor, cuadro, nro_radio):
        super().__init__(marca, modelo, num_ruedas, tipo)
        self.motor = motor
        self.cuadro = cuadro
        self.nro_radio = nro_radio

    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, ruedas:, {self.num_ruedas}, tipo de motocicleta: {self.tipo}, Motor: {self.motor}, tipo de cuadro: {self.cuadro}, Nro Radios: {self.nro_radio} "
