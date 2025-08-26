seleccionArgentina = {
    "10": {"Nombre": "Lionel Messi", "Edad": 35, "Altura": 1.70, "Precio": "18 Millones", "Posicion": "Extremo Derecho"},
    "19": {"Nombre": "Nicolas Otamendi", "Edad": 34, "Altura": 1.83, "Precio": "1 Millon", "Posicion": "Defensa Central"},
    "24": {"Nombre": "Nahuel Molina", "Edad": 27, "Altura": 1.75, "Precio": "20 Millones", "Posicion": "Lateral Derecho"},
    "22": {"Nombre": "Lautaro Martinez", "Edad": 27, "Altura": 1.74, "Precio": "95 Millones", "Posicion": "Delantero"},
    "3": {"Nombre": "Lisandro Martinez", "Edad": 26, "Altura": 1.75, "Precio": "50 Millones", "Posicion": "Defensa Central"},
    "20": {"Nombre": "Alexis Mac Allister", "Edad": 25, "Altura": 1.76, "Precio": "100 Millones", "Posicion": "Mediocampista"},
    "9": {"Nombre": "Julian Alvarez", "Edad": 24, "Altura": 1.70, "Precio": "100 Millones", "Posicion": "Delantero"},
    "8": {"Nombre": "Marcos Javier Acuña", "Edad": 33, "Altura": 1.72, "Precio": "2 Millones", "Posicion": "Lateral izquierdo"},
    "5": {"Nombre": "Leandro Paredes", "Edad": 31, "Altura": 1.80, "Precio": "5 Millones", "Posicion": "Pivote"}
}

for llave, valor in seleccionArgentina.items():
    print(llave, valor)

print("Tenemos cargados en el diccionario la cantidad de jugadores: ", end=" ")
print(len(seleccionArgentina))