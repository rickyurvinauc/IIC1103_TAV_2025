import amigos # Importar el modulo de amigos
# Leer el nombre
nombre = input()
# Imprimir el encabezado
print("Amigos reciprocos:")
# Iterar sobre los amigos. Debe ser desde 1 hasta la cantidad de amigos.
i = 1
# Obtener la cantidad de amigos del nombre dado
cantidad_amigos = amigos.numero(nombre)
# Mientras haya amigos
while i <= cantidad_amigos:
    # Obtener el amigo i del nombre dado
    amigo = amigos.obtener_amigo(nombre, i)
    # Verificar si el amigo obtenido tiene como amigo reciproco al nombre dado
    es_reciproco = False
    # Iterar sobre los amigos del amigo obtenido
    j = 1
    # Obtener la cantidad de amigos del amigo obtenido
    cantidad_del_amigo = amigos.numero(amigo)
    # Mientras haya amigos del amigo obtenido
    while j <= cantidad_del_amigo:
        # Si el amigo j del amigo obtenido es igual al nombre dado
        if amigos.obtener_amigo(amigo, j) == nombre:
            # Marcar como reciproco
            es_reciproco = True
        # Incrementar el contador para revisar el siguiente amigo del amigo obtenido
        j += 1
    # Si es reciproco, imprimir el nombre del amigo
    if  es_reciproco == True:
        print(amigo)
    # Incrementar el contador para revisar el siguiente amigo
    i += 1
