def equilibrado(palabra):
    # inicializar contadores
    vocales = 0
    consonantes = 0
    # recorrer la palabra completa
    for letra in palabra:
        # si letra es vocal:
        if letra in "aeiouAEIOU":
            # le sumo 1 al contador de vocales
            vocales +=1
        else: 
            # le sumo 1 al contador de consonantes
            consonantes +=1
    #la palabra es equilibrada en base a la diferencia absoluta entre consonantes y vocales
    equilibrio = abs(consonantes - vocales)
    return equilibrio


##################################
def equilibrado_v2(palabra):
    # inicializar contadores
    vocales = 0
    consonantes = 0
    # indice parte siendo 0 para el primer caracter de la palabra
    indice = 0
    # recorrer la palabra mientras el indice sea menor al largo de la palabra
    while indice < len(palabra):
        # si es que el caracger no pertenece a "aeiouAEIOU" tiene que ser consontante
        if palabra[indice] not in "aeiouAEIOU":
            # sumar +1 a consonantes
            consonantes +=1
        else: 
            # si no es consonante, es vocal (por enunciado)
            vocales +=1
        # avanzar el indice en 1
        indice+=1
    return abs(consonantes - vocales)

###################################

def equilibrado_v3(palabra):
    # inicializar contador de vocales
    vocales = 0
    # recorro la palabra
    for letra in palabra:
        # si letra es vocal
        if letra in "aeiouAEIOU":
            # si la letra es vocal sumo 1 al contador de vocales
            vocales += 1
    # calcular las consonantes en base al largo de la palabra sin vocales
    consonantes = len(palabra) - vocales
    # retornar la diferencia absoluta entre consonantes y vocales
    return abs(consonantes - vocales)
