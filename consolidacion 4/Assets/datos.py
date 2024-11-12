"""


Requerimientos:



se tienen los primeros datos: 


?1. Un vehículo contiene los siguientes atributos: marca, modelo y número de ruedas. 
?2. Un  automóvil  contiene  los  siguientes  atributos:  marca,  modelo,  número  de  ruedas, velocidad y cilindrada.




"""


"""
Clase padre --> Vehiculo: Marca, modelo y número de ruedas
Clase hijo --> Marca, modelo, número de ruedas, velocidad y cilindrada 

Hijo es dependiente de Padre 

Automovil dependiente de Vehiculo: Heredandole las siguientes caracteristicas --> Marca, Modelo, número de ruedas





"""

"""Parte 2 
Partiendo de la descripción anterior por parte del cliente, nos plantea que se manejan 
dos tipos de automóviles tipo: particular y carga -->

     que contienen todas las características de un automóvil.  
    ● Los automóviles tipo particular contienen adicionalmente los números de puesto.  
    ● Los automóviles tipo carga contienen adicionalmente el peso de la carga en kg. 
Adicionalmente, se tienen el tipo de vehículos que son 
bicicleta que contiene las características de los vehículos, y se le adiciona el tipo de bicicleta que puede ser: Urbana o de Carrera.  

Con los tipos de bicicletas tenemos las motocicletas que contienen todas las características de 
una bicicleta, además de las siguientes: nro_radios, cuadro y motor. 



"""

"""
Parte 2 
instanciamientos:
Motocicleta es instancia con relación a Vehículo:  True 
Motocicleta es instancia con relación a Automovil:  False 
Motocicleta es instancia con relación a Vehículo particular:  False 
Motocicleta es instancia con relación a Vehículo de Carga:  False 
Motocicleta es instancia con relación a Bicicleta:  True 
Motocicleta es instancia con relación a Motocicleta:  True
"""

"""Parte 3 """
