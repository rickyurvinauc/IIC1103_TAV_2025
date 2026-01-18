"""
Qué significa k-equilibrada?

Dada una palabra y un k:
Separamos la palabra en trozos de largo k
palabra[0:k], palabra[k:2k], palabra[2k:3k], ...
Evaluamos cada trozo:
Si todos son equilibrados → "k-equilibrada"
Si no es k-equilibrada, pero todos son equilibrados o semi → "semi-k-equilibrada"
Si alguno es no equilibrado → "no-k-equilibrada"
En cuanto aparece uno no equilibrado, se corta todo.
"""


# definir la función equilibrado que ya teníamos
def equilibrado(palabra):
    vocales = 0
    consonantes = 0
    for letra in palabra:
        if letra in "aeiouAEIOU":
            vocales +=1
        else: 
            consonantes +=1
    return abs(consonantes - vocales)

# definir la función auxiliar tipo_equilibrio
def tipo_equilibrio(palabra):
    equilibrio = equilibrado(palabra)
    if diferencia == 0:
        return "equilibrada"
    elif diferencia == 1:
        return "semi"
    else:
        return "no"

#####################################

# aqui lo hice sin usar la funcion auxiliar pero es lo mismo
def tipo_equilibrio(palabra):
    vocales = 0
    consonantes = 0

    for letra in palabra:
        if letra in "aeiouAEIOU":
            vocales += 1
        else:
            consonantes += 1

    diferencia = abs(vocales - consonantes)

    if diferencia == 0:
        return "equilibrada"
    elif diferencia == 1:
        return "semi"
    else:
        return "no"

#####################################

#funcion final pedida
def k_equilibrada(palabra, k):
    # suponer que es k-equilibrada y semi-k-equilibrada
    es_k_equilibrada = True
    es_semi_k_equilibrada = True
    #recorrer la palabra en trozos de largo k
    for inicio in range(0, len(palabra), k):
        # el primer trozo de palabra va de 0 a 0+k
        trozo = palabra[inicio: inicio + k]
        # determinar el tipo de equilibrio del trozo
        tipo = tipo_equilibrio(trozo)
        # trozo de tipo no equilibrada
        if tipo == "no":
            # k_equilibrada y semi_k_equilibrada son falsas porque ya sabemos que tiene un trozo no equilibrado
            es_k_equilibrada = False
            es_semi_k_equilibrada = False
            break
        elif tipo == "semi":
            # si es semi, k_equilibrada es falsa, porque ya sabemos que al menos un trozo no es equilibrado
            es_k_equilibrada = False

    # revisamos que obtuvimos con las variables booleanas
    if es_k_equilibrada == True:
        return "k-equilibrada"
    elif es_semi_k_equilibrada == True:
        return "semi-k-equilibrada"
    else:
        return "no-k-equilibrada"

########################################

# otra forma de hacer la funcion final pedida

def kequilibrada(palabra, k):
    # suponer que no hay semi equilibradas
    hay_semi = False
    # recorrer la palabra utilizando step k en el range con el parametro k de la funcion
    for i in range(0, len(palabra), k):
        # obtener el trozo de la palabra
        trozo = palabra[i:i+k]
        # obtener la diferencia absoluta entre vocales y consonantes del sub string (trozo de palabra)
        diferencia = equilibrado(trozo)
        # evaluar la diferencia
        if diferencia >= 2:
            return "no-k-equilibrada"
        elif diferencia == 1:
            # en este caso se encontro una semi equilibrada
            hay_semi = True

    if hay_semi == True:
        return "semi-k-equilibrada"
    else:
        return "k-equilibrada"
