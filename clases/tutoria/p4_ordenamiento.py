# Escribe tu código aquí
def criterio(item):
    # item -> [fecha, tiempo]
    return item[1]

def obtener_fechas_ocupadas(actividades):
    fechas = []

    for act in actividades:
        fecha = act[0]
        if fecha not in fechas:
            fechas.append(fecha)

    fechas_tiempos = []
    for fecha in fechas:
        # fecha -> "14/02"
        suma = 0
        for act in actividades:
            fecha2 = act[0]
            if fecha2 == fecha:
                # act[2] -> 120
                suma += act[2]
        fechas_tiempos.append([fecha, suma])
    
    fechas_tiempos.sort(key=criterio, reverse=True)
    resultado = []

    for item in fechas_tiempos:
        resultado.append(item[0])
    
    return resultado


# estrategia
# consturir una lista de fechas sin repeticion
# fechas = ["14/02","01/05","03/10"]

# fechas_tiempos = [
#     ["14/02", 165],
#     ["01/12", 240],
# ]