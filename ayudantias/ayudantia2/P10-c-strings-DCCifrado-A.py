def intercalado(frase):
    # string vacio para guardar frase secreta
    resultado = ""
    # bool auxiliar para saber si tomar o no el caracter
    tomar = False
    # recorrer cada caracter de la frase
    for c in frase:
        # si es + cambiar a tomar
        # si es - cambiar tomar = False
        if c == "+":
            tomar = True
        elif c == "-":
            tomar = False
        # si no es ni + ni - tengo que ver si es que debo toamr o no el siguiente caracter
        # si es que tomar = True lo guardo
        # si es que tomar = False no hago nada    
        else:
            #aqui yo tengo de c que puede ser Un caracter puede ser una letra minúscula o mayúscula, un espacio, o un símbolo especial (.!?,#@).
            if tomar == True:
                # concatenar caracter c al resultado
                resultado += c
    return resultado

#####################################

def intercalado(frase):
    resultado = ""
    # recorrer la frase de dos en dos caracteres
    for i in range(0, len(frase), 2):
        simbolo = frase[i] # puede ser "+" o "-"
        caracter = frase[i + 1] # puede ser una letra, espacio o simbolo especial
        # si es "+" concateno el caracter al resultado
        if simbolo == "+":
            resultado += caracter
    #retonar el resultado final
    return resultado
