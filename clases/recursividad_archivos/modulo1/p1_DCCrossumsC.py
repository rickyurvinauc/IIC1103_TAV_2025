def validez_fila(numeros, total):
    # Caso base 1: si la lista esta vacia y 
    # el total es cero, la suma fue correcta
    if len(numeros) == 0 and total == 0:
        return True
    
    # Caso base 2: si la lista esta vacia pero el 
    # total no llego a cero,la suma no coincide
    elif len(numeros) == 0 and total != 0:
        return False

    # Caso recursivo: resto el primer numero al total y 
    # llamo a la funcion con el resto de la lista
    total -= numeros[0]
    return validez_fila(numeros[1:], total)