#Tipo Set

planetas = {"Martes", "Jupiter", "Venus"}
print(len(planetas)) #Usamos la funsion len = length significa largo

#Revisar si un elemento existe dentro del set
print ("Jupiter" in planetas)

# Agregar un elemento
planetas.add("Tierra") #add es una funcion
print(planetas)

#Eliminar elementos, puede arrojar error si el elemento no existe
planetas.remove("Jupiter")
print(planetas)
planetas.discard("Tierra") #No da error, pero tampoco lo descarta si se ingresa mal el elemento
print(planetas)

#Limpiar set o conjunto
planetas.clear()
print(planetas)

#Eliminar set o conjunto
del planetas
#print(planetas) #Nos va a dar error