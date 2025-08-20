#Dada la siguiente tupla
tupla = (13, 1, 8, 3, 2, 5, 8) #Definimos la tupla

#A partir de la tupla definida crear una lista con los numeros < 5
lista = [] #Definimos la lista
#Filtramos los elementos menores a 5 de la tupla
for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)
print(lista)