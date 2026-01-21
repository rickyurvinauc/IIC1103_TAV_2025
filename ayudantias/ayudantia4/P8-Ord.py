def podio(tabla, continente):
    paises = []

    for fila in tabla:
        nombre = fila[0]
        cont = fila[1]
        oro = fila[2]
        plata = fila[3]
        bronce = fila[4]

        if continente == "*" or cont == continente:
            puntaje = 10 * oro + 5 * plata + bronce
            paises.append([nombre, puntaje])

    paises.sort(key=lambda x: (-x[1], x[0]))

    return paises[:3]

###########################################

def podio(tabla, continente):
    paises = []

    for nombre, cont, oro, plata, bronce in tabla:
        if continente == "*" or cont == continente:
            puntaje = 10 * oro + 5 * plata + bronce
            paises.append([nombre, puntaje])

    paises.sort(key=lambda x: (-x[1], x[0]))

    return paises[:3]
