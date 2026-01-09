# Escribe tu código aquí

def todos_los_nums(lista):
    lista.sort() # Ordenamos la lista
    # Recorremos la lista y comparamos cada índice con su valor
    for indice in range(len(lista)):
        # Si el índice no coincide con su valor, retornamos False
        if indice != lista[indice]:
            return False
    return True

