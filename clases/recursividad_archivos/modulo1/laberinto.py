# Funcion iterativa
def buscar_cuarto(edificio, numero):
    for indice_piso in range(len(edificio)):
        piso = edificio[indice_piso]
        for habitacion in piso:
            if habitacion == numero:
                return indice_piso + 1
    return -1


edificio = [
    [201, 202, 203],    
    [301, 302, 303],    
    [401, 402, 403],   
    [401, 402, 403],   
    [401, 402, 403],   
    [401, 402, 403]   
]
piso = [201, 202, 203]
# print(buscar_cuarto(edificio, 10))

def buscar_piso_recursivo(edificio, numero):
    piso = edificio[0]
    if numero in piso:
        return 1
    else:
        return 1 + buscar_piso_recursivo(edificio[1:], numero)
    
print(buscar_piso_recursivo(edificio, 302))


# Funcion con caso base cuando no encuentra el piso

  
def buscar_piso_recursivo(edificio, numero):
    # caso base 1: si no hay mas pisos
    if len(edificio) == 0:
        return -1

    piso = edificio[0]

    # caso base 2: si el numero esta en este piso
    if numero in piso:
        return 1

    # caso recursivo: buscar en los demas pisos
    resultado = buscar_piso_recursivo(edificio[1:], numero)

    # si no se encontro en los demas pisos, mantener -1
    if resultado == -1:
        return -1
    else:
        return 1 + resultado