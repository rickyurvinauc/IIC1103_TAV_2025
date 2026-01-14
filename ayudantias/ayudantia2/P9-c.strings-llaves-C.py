def casi_llave(p, q):
    # largo de la cadena q
    n = len(q)
    # recorrer la cadena p desde el indice 0 hasta len(p)-len(q)+1
    for i in range(len(p) - n + 1):
        # obtener la subcadena de p que va desde i hasta i+n
        # debe ser desde i hasta i+n porque debe tener el largo del string q
        p2 = p[i:i+n]
        # supongamos que es llave
        es_llave = True
        # este trozo de codigo es igual a funcion es_llave del ejercicio anterior
        # recorrer largo de string q
        for j in range(n):
            if p2[j].islower() != q[j].islower():
                es_llave = False
                break
        # si es que es_llave sigue siendo verdadera retornar True
        if es_llave == True:
            return True
    return False
###################################

# esta funcion copiada del ejercicio anterior
def son_llave(p, q):
    for i in range(len(p)):
        if p[i].islower() != q[i].islower():
            return False
    return True


def casi_llave(p, q):
    n = len(q)
    for i in range(len(p) - n + 1):
        trozo = p[i:i+n]
        if son_llave(trozo, q):
            return True
    return False
