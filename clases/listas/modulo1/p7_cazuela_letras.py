def solo_dcc(lista):
    # Recorro por indice para poder modificar la lista
    for indice_l in range(len(lista)):
        # Obtengo la letra en esa posicion
        letra = lista[indice_l]
        # Si la letra no es d ni c, la reemplazo por '-'
        if letra != 'd' and letra != 'c':
            lista[indice_l] = '-'
    # Devuelvo la lista modificada
    return lista