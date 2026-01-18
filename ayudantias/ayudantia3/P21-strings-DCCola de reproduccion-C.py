def siguiente(lista, cancion_actual):
    for cancion in lista:
        titulo, artista, indice_siguiente = cancion

        if titulo == cancion_actual:
            if indice_siguiente == -1:
                return "No disponible"
            else:
                return lista[indice_siguiente][0]

    return "No disponible"



#################

def siguiente(lista, cancion_actual):
    indice_siguiente = -1

    for i in range(len(lista)):
        if lista[i][0] == cancion_actual:
            indice_siguiente = lista[i][2]
            break

    if indice_siguiente == -1:
        return "No disponible"

    return lista[indice_siguiente][0]