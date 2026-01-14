def contar_minusculas_formaA(palabra):
    # contador de vocales minusculas
    vocales = 0
    # recorrer la palabra letra por letra
    for letra in palabra:
        # si es que letra pertenece a las vocales minusculas
        if letra in "aeiou":
            # incrementar el contador
            vocales +=1
    return vocales

mi_input=input()
print(contar_minusculas_formaA(mi_input))

#################################
def contar_minusculas_formaB(palabra):
    vocales = 0
    indice = 0
    while indice < len(palabra):
        if palabra[indice].islower() == True:
            vocales +=1
        indice+=1
    return vocales

mi_input=input()
print(contar_minusculas_formaB(mi_input))

##################################

def contar_minusculas_formaC(palabra):
    # contador de vocales minusculas
    vocales = 0
    # recorrer la palabra por indices
    for indice in range(len(palabra)):
        # si es que la letra en el indice es minuscula
        if palabra[indice].islower():
            vocales +=1
    return vocales

mi_input=input()
print(contar_minusculas_formaC(mi_input))

##################################

def contar_minusculas_formaD(palabra):
    vocales = 0
    for letra in palabra:
        if letra.isupper():
            continue
        else:
            vocales +=1
    return vocales

mi_input=input()
print(contar_minusculas_formaD(mi_input))