#DICCIONARIOS
"""
Definición: Un diccionario es una estructura que guarda datos en pares: cada dato tiene 
una clave (key) y un valor (value). Es como una agenda: buscás por nombre (clave) 
y encontrás el número (valor). 
"""

#"Maradona":10 #Maradona es la llave y el 10 es el tipo de dato que va a almacenar la llave, ambas partes forman al diccionario
#dict(key,value)
diccionario = {
    "IDE":"Integrated Development Environment", #Para finalizar un elemento en el diccionario hay que poner coma
    "POO":"Programación Orientada a Objetos",
    "SABD":"Sistema de Administración de Base de Datos "
}
print(len(diccionario)) #La función len nos muestra la cantidad de elementos que hay en el diccionario
print(diccionario)

#Acceder a un diccionario con la llave
print(diccionario["IDE"])

#Otra forma de acceder a un elemento
print(diccionario.get("POO"))
print(diccionario.get("SABD"))

#Modificamos elementos
diccionario["IDE"] = "Entorno de desarrollo integrado"
print(diccionario)

#Cómo recorrer/mostrar los elementos
for termino in diccionario: #Recorre mostrando solo las llaves
    print(termino)

#Necesitamos la función items para recorrer un diccionario
for termino, valor in diccionario.items():
    print(termino, valor)

#Otras maneras de acceder a un diccionario
for termino in diccionario.keys(): #Muestra solo las llaves
    print(termino)

for valor in diccionario.values(): #Muestra solo el valor
    print(valor)

#Comprobar la existencia de algún elemento
print("IDE" in diccionario) #Devuelve un booleano

#Agregar un elemento
diccionario["PK"] = "Primary Key"
print(diccionario)

#No es posible agregar llaves duplicadas al diccionario, si se agrega una llave existente sobreescribe
#con el nuevo valor

#Eliminar un elemento
diccionario.pop("SABD")
print(diccionario)

#Vaciar un diccionario
diccionario.clear()
print(diccionario)

#Eliminar diccionario
del diccionario #El diccionario se borra