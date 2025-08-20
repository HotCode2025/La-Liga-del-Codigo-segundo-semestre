#TUPLAS: sigue el oden de los elementos, pero a diferencia de las listas que son mutables (se puede eliminar/mofificar)
#las tuplas son inmutanbles.
#Definimos una tupla:
cocina = ("cuchara", "cuchillo", "tenedor") #Para las tuplas se usa parentesis
print(cocina)

#Saber la cantidad de elementos de la tupla:
print(len(cocina))

#Acceder a un elemento, para esto se utilizan corchetes no parentesis
print(cocina[0])
#Mostrar de manera inversa
print(cocina[-1])

#Acceder a un Rango
print(cocina[0:2])
#Ejemplo
verduras = ["papa"] #Las tuplas siempre deben llevar "," aunque sea solo un elemento, sino dejan de ser tuplas y pasan a ser string

# Recorremos los elementos de la tupla
for cocinar in cocina:  #Print está usando \n para saltos de linea, para solucionarlo se utiliza la función end
    print(cocinar, end=" ")

#LA UNICA MANERA DE MODIFICAR UNA TUPLA: es pasarlo de tupla a lista, y luego de lista a tupla, (no es una buena práctica)
cocinaLista = list(cocina) #De tupla a lista
cocinaLista[0] = "Plato"   #Modificar posición
cocina = tuple(cocinaLista) #De lista a tupla
print("\n", cocina) #Anulamos con \n el end anterior


#del  cocina  Esto es para eliminar una tupla