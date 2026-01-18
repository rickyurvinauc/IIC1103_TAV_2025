restaurante = [
  ["P","S","P"],   # fila 0
  ["C","S","S"],   # fila 1
  ["S","M","C"]    # fila 2
]

def encontrar_mesero(restaurante):
    # indice_f = 0
    # for fila in restaurante:
    #     if "M" in fila:
    #         indice_c = fila.index("M")
    #         return [indice_f, indice_c]
    #     indice_f += 1
    for indice_f in range(len(restaurante)):
        for indice_c in range(len(restaurante[0])):
            elemento = restaurante[indice_f][indice_c]
            if elemento == "M":
                return [indice_f, indice_c]

print(encontrar_mesero(restaurante))