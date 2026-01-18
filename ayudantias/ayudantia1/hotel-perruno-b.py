import hotel # Importar el modulo del hotel

def revisar_asignacion():
    # Revisar si hay perros con asignacion repetida
    habitaciones = hotel.num_habitaciones()
    repetidos = 0
    # Iterar sobre todas las habitaciones
    i = 0
    while i < habitaciones:
        # Obtener el nombre del perro en la habitacion i
        perro = hotel.nombre_ocupante(i)
        # Verificar si ya se conto este perro
        ya_contado = False
        # Buscar en las habitaciones anteriores
        k = 0
        # Mientras no se haya contado y queden habitaciones por revisar
        while k < i:
            # Si el perro ya fue contado
            if hotel.nombre_ocupante(k) == perro:
                # Marcar como contado
                ya_contado = True
            # Incrementar k
            k += 1
        # Si no se habia contado antes
        if ya_contado == False:
            # Contar cuantas veces aparece este perro
            conteo = 0
            # Buscar en todas las habitaciones
            j = 0
            while j < habitaciones:
                # Si el perro en la habitacion j es el mismo
                if hotel.nombre_ocupante(j) == perro:
                    # Incrementar el conteo
                    conteo += 1
                # Incrementar  j
                j += 1
            # Si el conteo es mayor a 1, hay repetidos
            if conteo > 1:
                # Incrementar el numero de repetidos
                repetidos += 1
        # Incrementar i
        i += 1
    return repetidos
