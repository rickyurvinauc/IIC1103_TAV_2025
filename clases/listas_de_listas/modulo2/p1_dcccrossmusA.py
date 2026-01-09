def borrar_fila(tablero, f):
    fila = tablero[f]
    primer_numero = fila[0]
    for indice_f in range(1, len(fila)):
        num = fila[indice_f]
        if num > primer_numero:
            fila[indice_f] = 0
    return tablero