peliculas = [
    ["Una nueva esperanza", 1997, "Ciencia ficción","Un joven granjero intercepta una llamada de socorro", [8, 9], 8.5],
    ["La amenaza fantasma", 1999, "Ciencia ficción","Los Jedi descubren a Anakin Skywalker", [9, 10], 9.5],
    ["Dunkirk", 2017, "Guerra","Dramática evacuación en la Segunda Guerra Mundial", [7, 8], 7.5],
]

# quiero la categoria de la segunda película
categoria = peliculas[1][2]   # ¿que era el [2]? (numero mágico)

# anadir un puntaje a la primera película
peliculas[0][4].append(10)    # [4] era 'puntos' (pero no se entiende)


# se agrega puntaje, pero si olvido recomputar el promedio, quedan datos inconsistentes
peliculas[1][4].append(6)
# uy, falto esto...
peliculas[1][5] = round(sum(peliculas[1][4]) / len(peliculas[1][4]), 1)


# contar cuantas por anio
conteo = []  # cada item sera [anio, cantidad]
for fila in peliculas:
    anio = fila[1]  # indice 1 = anio
    encontrado = False
    for item in conteo:
        if item[0] == anio:
            item[1] += 1
            encontrado = True
            break
    if not encontrado:
        conteo.append([anio, 1])

# filtrar por categoria
categoria_objetivo = "Ciencia ficcion"
resultado = []
for fila in peliculas:
    categoria = fila[2]  # indice 2 = categoria
    if categoria_objetivo in categoria:
        resultado.append(fila)