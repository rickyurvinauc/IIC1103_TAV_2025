def buscar_sin_respuesta(invitados, confirmaciones):
    asistentes = []
    # Se crea una lista vacia donde se guardaran los invitados que no han respondido
    for invitado in invitados:
        # Se recorre cada nombre en la lista de invitados
        ultima_resp = ""
        # Se inicializa una variable para guardar la ultima respuesta encontrada del invitado
        # Si no se encuentra ninguna, se mantendra como cadena vacia
        for confirmacion in confirmaciones:
            # Se recorre cada elemento de la lista de confirmaciones
            # Cada confirmacion es una lista con dos elementos: [nombre, respuesta]
            if invitado == confirmacion[0]:
                # Si el nombre del invitado coincide con el de la confirmacion...
                ultima_resp = confirmacion[1]
                # se actualiza 'ultima_resp' con la respuesta correspondiente
        if ultima_resp == "":
            # Si despues de revisar todas las confirmaciones, no se encontro ninguna respuesta...
            asistentes.append(invitado)
            # se agrega ese invitado a la lista de asistentes sin respuesta
    return asistentes
    # Al final, se devuelve la lista de invitados que no tienen ninguna confirmacion registrada