#"Maradona": 10 Un diccionario esta compuesto por dos elementos
# Una Llave y un Valor
#dict(key,value)
diccionario = {
    "IDE": "Integrated Development Environment",
    "POO": "Programacíon Orientada a Objetos",
    "SABD": "Sistema de Administracion de Base de Datos"
}

#Verificar la cantidad de elementos del diccionario
print(len(diccionario))
print(diccionario)

#Acceder a un diccionario con la llave(key)
print(diccionario["IDE"])

#Otra forma de recuperar un elemento
print(diccionario.get("POO"))
print(diccionario.get("SABD"))

#Modificamos elementos
diccionario["IDE"] = "Entorno de Desarrollo Integrado"
print(diccionario)

#Como recorrer los elementos
for termino in diccionario:
    print(termino)

#Necesitamos una funcion para recorrer un diccionario
for termino, valor in diccionario.item():
    print(termino, valor)

#Otras maneras de acceder a un diccionario
for termino in diccionario.keys():
    print(termino) #Muestra una sola llave

for valor in diccionario.values(): #Usamos una fucion para acceder a un valor
    print(valor)

#Comprobar la existencia de algun elemento
print("IDE" in diccionario) #Devuelve un boolean

#Agregar un elemento
diccionario["PK"] = "Primer key"
print(diccionario)

#Eliminar un elemento
diccionario.pop("SABD")
print(diccionario)

#Eliminar diccionario
del diccionario #el diccionario se borro