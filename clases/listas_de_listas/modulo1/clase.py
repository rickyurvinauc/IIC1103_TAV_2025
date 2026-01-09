restaurante = [
  ["P","S","P"],   # fila 0
  ["C","M","S"],   # fila 1
  ["S","P","C"]    # fila 2
]

def buscar_mesero(restaurante, elemento):

    indice_f = 0
    for fila in restaurante:
        if elemento in fila:
            indice_col = fila.index(elemento)
            break
        indice_f += 1
    
    return [indice_f, indice_col]

posicion_mesero = buscar_mesero(restaurante, "S")
print(posicion_mesero)


