def borrar_col(tablero, c):
    numero = tablero[0][c]
    for indice_f in range(len(tablero)):
        for indice_c in range(len(tablero[0])):
            if indice_c == c:
                num = tablero[indice_f][indice_c]
                if num > numero:
                    tablero[indice_f][indice_c] = 0
    return tablero