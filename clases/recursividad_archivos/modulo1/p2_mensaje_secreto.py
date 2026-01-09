# letras = ['r', 'g', 'a', 'p', 't', 'b', 'b', 'a', 't', 'o', 's']
# instrucciones = ['ignorar', 1, 'agregar', 2, 'ignorar', 1, 'agregar', 1, 'ignorar', 4, 'agregar', 2]

# Funcion recursiva que toma una lista de letras y una lista de instrucciones
# Cada instruccion tiene dos partes: una accion ("agregar" o cualquier otra) y una cantidad
# La idea es ir procesando las instrucciones de dos en dos

def descifrar_rec(letras, instrucciones):
    # Caso base: si quedan solo dos elementos en la lista de instrucciones
    if len(instrucciones) == 2:
        accion = instrucciones[0]
        cantidad = instrucciones[1]
        # Si la accion es "agregar", devuelve las primeras "cantidad" letras
        if accion == "agregar":
            return letras[:cantidad]
        # Si no, devuelve una lista vacia
        else:
            return []

    # Si aun quedan mas instrucciones, tomo la primera accion y cantidad
    accion = instrucciones[0]
    cantidad = instrucciones[1]

    # Si la accion es "agregar", tomo las primeras "cantidad" letras
    # y luego llamo recursivamente para procesar el resto de las letras y las instrucciones restantes
    if accion == "agregar":
        return letras[:cantidad] + descifrar_rec(letras[cantidad:], instrucciones[2:])
    else:
        # Si la accion no es "agregar", simplemente salto esas letras
        # y sigo con la siguiente parte de las instrucciones
        return descifrar_rec(letras[cantidad:], instrucciones[2:])

# 1. descifrar_rec(['r', 'g', 'a', 'p', 't', 'b', 'b', 'a', 't', 'o', 's'], ['ignorar', 1, 'agregar', 2, 'ignorar', 1, 'agregar', 1, 'ignorar', 4, 'agregar', 2])
# 2. descifrar_rec([ 'g', 'a', 'p', 't', 'b', 'b', 'a', 't', 'o', 's'], [ 'agregar', 2, 'ignorar', 1, 'agregar', 1, 'ignorar', 4, 'agregar', 2])
# 3. [ 'g', 'a'] + descifrar_rec([ 'p', 't', 'b', 'b', 'a', 't', 'o', 's'], [ 'ignorar', 1, 'agregar', 1, 'ignorar', 4, 'agregar', 2])
# 4.  descifrar_rec([ 't', 'b', 'b', 'a', 't', 'o', 's'], [  'agregar', 1, 'ignorar', 4, 'agregar', 2])
# 5.  [ 't'] + descifrar_rec([ 'b', 'b', 'a', 't', 'o', 's'], [ 'ignorar', 4, 'agregar', 2])
# 6.  descifrar_rec([ 'o', 's'], [ 'ignorar', 4, 'agregar', 2])
# 6.  [ 'o', 's']

# Resultado ->[ 'g', 'a']+ [ 't'] + [ 'o', 's']