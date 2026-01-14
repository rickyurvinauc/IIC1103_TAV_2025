def es_vocal(c):
    # retorna True si c es vocal, False en caso contrario
    return c in "aeiouAEIOU"

def intercalado(palabra):
    # recorremos la palabra y verificamos que cada caracter
    for i in range(len(palabra) - 1):
        #vemos si el caracter palabra[i] y el siguiente palabra[i + 1] son ambos vocales o ambos consonantes
        if es_vocal(palabra[i]) == es_vocal(palabra[i + 1]):
            # si ambos son vocales no estan intercalados consonantes con vocal
            return False
    #en caso contrario, si recorrimos toda la palabra sin encontrar dos vocales o dos consonantes juntas, estan intercalados
    return True

def completamente_equilibrada(palabra):
    if len(palabra) % 2 != 0:
        return False

    # inicializar contador de vocales 
    vocales = 0
    # recorrer la palabra contando vocales
    for c in palabra:
        if es_vocal(c):
            vocales += 1
    # calcular consonantes en base al largo de la palabra sin vocales
    consonantes = len(palabra) - vocales
    #cantidad de vocales igual a cantidad de consonantes 
    #y ademas intercalado(palabra) debe ser verdadero para que sean intercaladas
    return vocales == consonantes and intercalado(palabra)

def mayor_trozo_completamente_equilibrado(palabra):
    # inicializar mejor trozo encontrado
    mejor = ""
    # n va a ser el largo de la palabra
    n = len(palabra)
    # recorrer todos los posibles trozos de la palabra
    for i in range(n):
        # j va desde i+1 hasta n+1 para considerar todos los trozos que empiezan en i
        for j in range(i + 1, n + 1):
            trozo = palabra[i:j]
            # si el trozo es menor o igual al mejor encontrado hasta el momento, no sirve
            if len(trozo) <= len(mejor):
                continue
            if completamente_equilibrada(trozo) == True:
                mejor = trozo
    # retornar el mejor encontrado final
    return mejor


##########################################################
# otra solucion solo utilizando la funcion de es_vocal(c)

def mayor_trozo_completamente_equilibrado(palabra):
    mejor = ""
    n = len(palabra)

    i = 0
    while i < n - 1:
        inicio = i

        # Construir tramo intercalado máximo
        # mientras los caracteres sean alternadamente vocal y consonante
        while i + 1 < n and es_vocal(palabra[i]) != es_vocal(palabra[i + 1]):
            # avanzar el índice
            i += 1
        # Al salir del bucle, i está en el último carácter del tramo
        fin = i + 1
        # Obtener el tramo
        tramo = palabra[inicio:fin]

        # Solo largos pares pueden ser equilibrados porque tienen mitad vocales y mitad consonantes
        largo = len(tramo)
        # Verificar si el tramo es equilibrado
        if largo >= 2:
            # si es impar, quitar el último carácter para hacerlo par
            if largo % 2 != 0:
                tramo = tramo[:-1]
            # Verificar si es mejor que el mejor encontrado hasta ahora
            if len(tramo) > len(mejor):
                # Actualizar el mejor tramo encontrado
                mejor = tramo
        # Avanzar al siguiente carácter para iniciar un nuevo tramo
        i += 1

    return mejor
