def hacer_grandioso(lista_magos):

  for i in range(len(lista_magos)):
    lista_magos[i] = "El gran " + lista_magos[i]

def imprimir_nombres(lista):

  for nombre in lista:
    print(nombre)

# Diccionarios
nombres = ["Harry Houdini", "Newton", "David Blaine", "Hawking", "Messi", "Teller", "Einstein", "Pele", "Juanes"]
magos = ["Harry Houdini", "David Blaine", "Teller"]
cientificos = ["Newton", "Hawking", "Einstein"]
otros = [nombre for nombre in nombres if nombre not in magos and nombre not in cientificos] # for para identificar a otros 


#prints generales

print("Lista original:")
imprimir_nombres(nombres) # lista original 


hacer_grandioso(magos) # hacemos grandiosos a los magos


print("\nMagos grandiosos:")  
imprimir_nombres(magos) 

print("\nCientificos:")
imprimir_nombres(cientificos)

print("\nOtros:")
imprimir_nombres(otros)