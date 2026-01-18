def artista_favorito(lista):
    artistas = []
    conteos = []

    for cancion in lista:
        artista = cancion[1]

        if artista in artistas:
            indice = artistas.index(artista)
            conteos[indice] += 1
        else:
            artistas.append(artista)
            conteos.append(1)

    max_canciones = conteos[0]
    favorito = artistas[0]

    for i in range(1, len(conteos)):
        if conteos[i] > max_canciones:
            max_canciones = conteos[i]
            favorito = artistas[i]

    return favorito


###############


def artista_favorito(lista):
    #inicializar variables para llevar el conteo maximo y el artista favorito
    max_canciones = 0
    favorito = ""

    #recorrer la lista de canciones por indice
    for i in range(len(lista)):
        #obtener el artista de la canción actual
        artista_actual = lista[i][1]
        #inicializar el contador de canciones para el artista actual
        contador = 0

        #recorrer la lista nuevamente para contar las canciones del artista actual
        for j in range(len(lista)):
            #verificar si la canción actual es del artista actual
            if lista[j][1] == artista_actual:
                #incrementar el contador para el artista actual
                contador += 1
        #verificar si el contador del artista actual es mayor que el maximo registrado
        if contador > max_canciones:
            #actualizar el maximo y el artista favorito
            max_canciones = contador
            favorito = artista_actual
    #retorno artista favorito
    return favorito