import hotel # Importar el modulo del hotel

def se_puede_excursion(cantidad):
    # Determinar si se pueden llevar los perros de excursion
    timidos = 0 #  contador de perros timidos
    extrovertidos = 0 # contador de perros extrovertidos
    habitaciones = hotel.num_habitaciones() # obtengo numero de habitaciones
    i = 0 # contador de habitaciones
    # recorro todas las habitaciones
    while i < habitaciones: 
        # obtengo nombre del perro de la habitacion i
        perro = hotel.nombre_ocupante(i)
        # obtengo caracter del perro timido o extrovertido
        caracter = hotel.obtener_caracter(perro)
        # incremento el contador segun el caracter del perro obtenido
        if caracter == "timido":
            # si el caracter es timido incremento contador de perros timidos
            timidos += 1
        else:
            # si el caracter es extrovertido incremento contador de perros extrovertidos
            extrovertidos += 1
        # incremento el contador de habitaciones para seguir recorriendo
        i += 1

    # Cada bus tiene capacidad para 5 perros
    # Debo sumar 4 porque si hay un perro mas de un multiplo de 5 necesito otro bus adicionalmente
    buses_timidos = (timidos + 4) // 5
    buses_extrovertidos = (extrovertidos + 4) // 5

    # Total de buses necesarios
    buses_necesarios = buses_timidos + buses_extrovertidos

    # Comparo cantidad de buses disponibles con los necesarios
    if cantidad >= buses_necesarios:
        print(f"Suficientes: se tienen {cantidad} y se necesitan {buses_necesarios}")
    else:
        print(f"Insuficientes: se tienen {cantidad} y se necesitan {buses_necesarios}")
