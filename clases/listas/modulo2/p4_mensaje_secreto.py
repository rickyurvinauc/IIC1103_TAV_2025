# Escribe tu código aquí

def descifrar_it(letras, instrucciones):
    lista_final = []
    indices_anteriores = 0
    # Recorremos las instrucciones de dos en dos
    for indice_i in range(0, len(instrucciones), 2):
        # Obtenemos la acción actual
        accion = instrucciones[indice_i]
        # Si la acción es "agregar", agregamos las letras correspondientes a la lista final
        if accion == "agregar":
            # Cantidad de letras a agregar
            cant = instrucciones[indice_i + 1]  # 1
            for i in range(cant):
                # Agregamos la letra correspondiente a la lista final
                lista_final.append(letras[indices_anteriores + i])
        # Si la acción es "saltar", simplemente actualizamos el índice de las letras
        indices_anteriores += instrucciones[indice_i + 1]
        indice_i += 1
    return lista_final



