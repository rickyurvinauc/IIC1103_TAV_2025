def podio(tabla, continente):
    # incializar lista de paises
    paises = []

    # recorrer la tabla 
    # cada fila es un pais de la tabla
    for fila in tabla:
        nombre = fila[0] # nombre del pais
        cont = fila[1] # nombre continente del pais
        oro = fila[2] # cantidad de medallas de oro
        plata = fila[3] # cantidad de medallas de plata
        bronce = fila[4] # cantidad de medallas de bronce

        # si el continente es "*" o el continente del pais es igual al continente dado
        if continente == "*":
            puntaje = 10 * oro + 5 * plata + bronce
            paises.append([nombre, puntaje])
            
             or cont == continente:
            # calcular puntaje, con formula del enunciado
            puntaje = 10 * oro + 5 * plata + bronce
            # una vez calculo el puntaje agrego el pais a la lista de paises
            paises.append([nombre, puntaje])
    # lambda lleva a cabo la ordenacion segun los criterios pedidos
    # primero por puntaje descendente, luego por nombre ascendente
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
