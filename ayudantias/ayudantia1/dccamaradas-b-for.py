import amigos # Importar el modulo de amigos
nombre = input() # Leer el nombre
print("Amigos reciprocos:") # Imprimir el encabezado
# Obtener la cantidad de amigos del nombre dado
cantidad_amigos = amigos.numero(nombre)
# Iterar sobre los amigos. Debe ser desde 1 hasta la cantidad de amigos.
# se suma 1 porque el rango no incluye el ultimo numero
for i in range(1, cantidad_amigos + 1):
    # Obtener el amigo i del nombre dado
    amigo = amigos.obtener_amigo(nombre, i)
    # Obtener la cantidad de amigos del amigo obtenido
    cantidad_del_amigo = amigos.numero(amigo)
    # Verificar si el amigo obtenido tiene como amigo reciproco al nombre dado
    # se suma 1 porque el rango no incluye el ultimo numero
    for j in range(1, cantidad_del_amigo + 1):
        # Si el amigo j del amigo obtenido es igual al nombre dado
        if amigos.obtener_amigo(amigo, j) == nombre:
            # Imprimir el nombre del amigo reciproco
            print(amigo)
            # Salir del ciclo interno ya que se encontro la reciprocidad
            break
