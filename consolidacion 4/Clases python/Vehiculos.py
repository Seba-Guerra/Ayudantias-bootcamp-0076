
#!clase padre
class Vehiculo:
    def __init__(self, marca, modelo, num_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.num_ruedas = num_ruedas

    # ? atributo adicional de formato string especifico en el cual me entregará: Marca x | Modelo y | xy ruedas
    def __str__(self):  # ? Hey soy un texto = __str__ que se considere como atributo
        # almacenando información
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.num_ruedas} ruedas"

#!clase padre


class Automovil(Vehiculo):
    def __init__(self, marca, modelo, num_ruedas, velocidad, cilindraje):
        # ! Hay una relación entre Padre (Vehiculos) hacia Hijo (Automovil)
        # ? Atributos Generales (Padre)
        super().__init__(marca, modelo, num_ruedas)
        # ? Atributos particulares (Hijo)
        self.velocidad = velocidad
        self.cilindraje = cilindraje

        def __str__(self):  # ? Hey soy un texto = __str__ que se considere como atributo
            # almacenando información
            return f"Marca {self.marca}, Modelo {self.modelo}, {self.num_ruedas} ruedas, {self.velocidad} velocidad, {self.cilindraje} velocidad"


# considerando la información almacenada
# almacenando información velocidad
