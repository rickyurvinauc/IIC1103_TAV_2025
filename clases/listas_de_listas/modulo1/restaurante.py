restaurante = [
  ["P","S","P"],   # fila 0
  ["C","M","S"],   # fila 1
  ["S","P","C"]    # fila 2
]
print(restaurante[1])     
# fila 1 -> ['C', 'M', 'S']
print(restaurante[2][2])  
# elemento en fila 2, col 2 -> "C"

def buscar_mesero(restaurante):
    indice_fila = 0
    indice_columna = -1
    for fila in restaurante:
        if "M" in fila:
            indice_columna = fila.index("M")
            break
        indice_fila += 1
    
    return [indice_fila, indice_columna]

posicion_mesero = buscar_mesero(restaurante)
print(posicion_mesero)
# [1, 1]

fila, col = posicion_mesero
# mover arriba si es valido
if fila - 1 >= 0:
    # ahora la posicion del mesero es ocupado por una silla
    restaurante[fila][col] = "S"
    fila -= 1
    # ahora la posicion de a donde se movio esta el Mesero
    print("Mesero ahora en:", fila, col)
    restaurante[fila][col] = "M"

for fila in restaurante:
    print(fila)

# ['P', 'M', 'P']
# ['C', 'S', 'S']
# ['S', 'P', 'C']

fila, col = buscar_mesero(restaurante)
# mover izquierda si es valido
if col - 1 >= 0:
    restaurante[fila][col] = "S"
    col -= 1
    print("Mesero ahora en:", fila, col)
    restaurante[fila][col] = "M"

for fila in restaurante:
    print(fila)

# Mesero ahora en: 0 0
# ['M', 'S', 'P']
# ['C', 'S', 'S']
# ['S', 'P', 'C']