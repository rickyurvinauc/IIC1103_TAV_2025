import amigos # Importar el modulo de amigos
# Leer el nombre 
nombre = input()
# Obtener la carrera del amigo
carrera = amigos.estudia(nombre)

print("Amigos de mi amigo:")

# Iterar sobre los amigos del amigo dado, comienza en 1 de acuerdo a enunciado
i = 1
# Mientras haya amigos
while True:
    # Obtener el siguiente amigo
    amigo = amigos.obtener_amigo(nombre, i)
    # Si no hay mas amigos, salir del ciclo
    if amigo == "":
        # Salir del ciclo
        break
    # Si el amigo estudia la misma carrera
    if amigos.estudia(amigo) == carrera:
        # Imprimir el nombre del amigo
        print(amigo)
    # Incrementar el contador para revisar el siguiente amigo
    i += 1
