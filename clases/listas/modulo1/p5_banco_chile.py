def contabilizar(lista):
    dep_total = 0
    ret_total = 0
    # Recorro por indice para poder modificar la lista
    for i_lista in range(len(lista)):
        # Obtengo el numero en esa posicion
        numero = lista[i_lista]
        # Si el numero es positivo, lo sumo a dep_total
        # Si es negativo, lo sumo a ret_total
        if numero > 0:
            dep_total = dep_total + numero
        else:
            ret_total = ret_total + numero
    # Armo la lista de respuesta
    lista_respuesta = [dep_total, ret_total]
    return lista_respuesta
