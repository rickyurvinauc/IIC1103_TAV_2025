
def primera_cancion(lista):
    """
    Esta función identifica la primera canción de la lista recorriendo todas las canciones 
    y verificando cuáles son mencionadas como 'siguiente' por otra canción. La primera canción 
    es aquella que no aparece como 'siguiente' en ninguna otra, es decir, nadie la enlaza antes, 
    por lo que necesariamente es el inicio de la secuencia. Así, al buscar el índice que no está 
    en la lista de 'siguientes', encontramos la primera canción.
    """
    #lista para guardar los indices de las canciones que son siguientes de otra
    siguientes = []
    # llenar la lista con los indices de las canciones que son siguientes
    for cancion in lista:
        # verificar si la canción tiene un siguiente
        if cancion[2] != -1:
            #guardar en la lista de siguientes canciones
            siguientes.append(cancion[2])
    # recorrer la lista original para encontrar la primera canción
    for i in range(len(lista)):

        # si el indice de la canción no esta en la lista de siguientes, es la primera
        if i not in siguientes:
            # retornar el nombre de la primera canción
            return lista[i][0]


#####################

def primera_cancion(lista):
    # recorrer la lista de canciones por indice
    for i in range(len(lista)):
        #asumir que la canción i es la primera
        es_primera = True

        #verificar si alguna canción tiene a i como siguiente
        for cancion in lista:
            # verifico si la canción actual tiene como siguiente a la canción i
            if cancion[2] == i:
                # la canción i no es la primera
                es_primera = False
                # break para no seguir recorriendo el for
                break
        # si es que la canción i es la primera
        if es_primera == True:
            return lista[i][0]