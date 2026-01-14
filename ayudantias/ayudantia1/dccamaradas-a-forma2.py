import amigos # Importar el modulo de amigos
# Leer el nombre
nombre = input()
# Obtener la carrera del amigo
carrera = amigos.estudia(nombre)

print("Amigos de mi amigo:")
# Iterar sobre los amigos del amigo dado, comienza en 1 de acuerdo a enunciado
i = 1
# Obtener el primer amigo
amigo = amigos.obtener_amigo(nombre, i)
# Mientras haya amigos
while amigo != "":
    # Si el amigo estudia la misma carrera
    if amigos.estudia(amigo) == carrera:
        # Imprimir el nombre del amigo
        print(amigo)
    # Incrementar el contador para revisar el siguiente amigo
    i += 1
    # Obtener el siguiente amigo
    amigo = amigos.obtener_amigo(nombre, i)
