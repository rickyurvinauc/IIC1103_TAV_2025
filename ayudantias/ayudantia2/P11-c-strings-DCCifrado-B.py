def encadenado(frase):
    #partimos con un string vacio
    resultado = ""
    # recorrer cada caracter de la frase que es parametro de la funcion
    for i in range(len(frase)):
        # si el caracter es un digito
        if frase[i].isdigit() == True:
            # comenzamos desde i+1 porque no debo considerar el digito
            # llegamos hasta i + el valor numerico del digito + 1 
            resultado += frase[i+1 : i + int(frase[i]) + 1]
    return resultado

###########################################################

def encadenado(frase):
    # resultado que parte siendo string vacio
    resultado = ""
    # indice que parte en 0, porque es el primer caracter de mi frase
    i = 0

    # mientras que i sea menor al largo de la frase
    while i < len(frase):
        if not frase[i].isdigit():
            i += 1
            continue
        n = int(frase[i])
        resultado += frase[i+1: i+1+n]
        i += 1 + n

    return resultado

###########################################################

def encadenado(frase):
    resultado = ""
    for i in range(len(frase)):
        if frase[i] in "0123456789":
            resultado += frase[i+1 : i + int(frase[i]) + 1]
    return resultado

