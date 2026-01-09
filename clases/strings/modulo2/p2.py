def agregar_puntos(texto):
    cadena_final = ""
    j = 0
    for i in range(1, len(texto)):
        letra = texto[i] # S
        if letra.isupper(): # i -> 20
            cadena_final += texto[j:i-1]+". "
            j = i
    cadena_final += texto[j:] +"."
    return cadena_final