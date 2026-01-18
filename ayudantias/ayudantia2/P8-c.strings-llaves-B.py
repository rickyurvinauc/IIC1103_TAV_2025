def son_llave(p, q):
    # Recorrer los caracteres de la palabra p
    for i in range(len(p)):
        # p[i] = caracter en la posicion i de la cadena p
        # q[i] = caracter en la posicion i de la cadena q
        # si es que p[i] es minuscula, necesito que q[i] tambien sea minuscula
        if p[i].islower() != q[i].islower():
            return False
    return True


###################################

def son_llave(p, q):
    for i in range(len(p)):
        # verificar si ambos caracteres son mayusculas o ambos son minusculas
        if p[i].isupper() != q[i].isupper():
            return False
    return True


###################################

def son_llave_con_while(p, q):
    indice = 0
    while indice < len(p):
        if p[indice].islower() != q[indice].islower():
            return False
        indice += 1
    return True
    
####################################

def son_llave_con_while(p, q):
    indice = 0
    while indice < len(p):
        if p[indice].islower() == q[indice].islower() or p[indice].isupper() == q[indice].isupper():
            pass
        else:
            return False
        indice += 1
    return True
###################################

