def criterio(item):
    return -item[1], item[0]

def podio(tabla, continente):
    lista_res = []
    for p in tabla:
        puntos = p[2]*10 + p[3]*5 + p[4]
        lista_res.append([p[0], puntos, p[1]])
    lista_res.sort(key=criterio)
    lista_f = []
    if continente == "*":
        for indice_p in range(3):
            p = lista_res[indice_p]
            lista_f.append([p[0],p[1]])
    else:
        contador = 0
        for indice_p in range(len(lista_res)):
            p = lista_res[indice_p]
            if contador <3 and p[2] == continente:
                lista_f.append([p[0],p[1]])
                contador += 1
    return lista_f