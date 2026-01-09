def obtener_confirmados(respuestas):
    asistentes = []
    # Se inicializa una lista vacia para guardar los nombres de los invitados confirmados

    for respuesta in respuestas:
        # Se recorre cada respuesta de la lista
        nombre = respuesta[0]
        # Se extrae el nombre del invitado desde la respuesta actual
        if nombre not in asistentes:
            # Si el nombre todavia no ha sido agregado a la lista de asistentes...
            ultima_resp = ""
            # Se inicializa una variable para guardar la ultima respuesta encontrada para ese nombre
            for confirmacion in respuestas:
                # Se recorre nuevamente la lista completa de respuestas
                if nombre == confirmacion[0]:
                    # Si el nombre coincide con el de la confirmacion actual...
                    ultima_resp = confirmacion[1]
                    # se actualiza la ultima respuesta
            if ultima_resp == "si":
                # Si la ultima respuesta encontrada es "si"...
                asistentes.append(nombre)
                # se agrega el nombre a la lista de asistentes
    return asistentes
    # Se retorna la lista final de nombres que confirmaron "si" en su ultima respuesta