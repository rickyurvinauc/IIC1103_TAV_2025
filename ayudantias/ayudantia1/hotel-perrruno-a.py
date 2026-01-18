import hotel # Importar el modulo del hotel

def obtener_habitacion(nombre):
    # Obtener la habitacion del perro con el nombre dado
    habitaciones = hotel.num_habitaciones()
    # Buscar en todas las habitaciones
    numero_habitacion = 0
    while numero_habitacion < habitaciones:
        # Si el perro en la habitacion es el que buscamos
        if hotel.nombre_ocupante(numero_habitacion) == nombre:
            return numero_habitacion
        # Incrementar el numero de habitacion
        numero_habitacion += 1
        
    # Si no se encontro, retornar -1
    return -1
