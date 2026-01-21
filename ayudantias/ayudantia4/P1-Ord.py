# Leer archivo y guardar participantes
def dccshow():
    participantes = []

    with open("talentos.txt", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if linea == "":
                continue

            datos = linea.split(";")
            nombre = datos[0]
            email = datos[1]
            major = datos[2]
            actuacion = int(datos[3])
            canto = int(datos[4])
            baile = int(datos[5])

            suma = actuacion + canto + baile
            participantes.append([nombre, email, major, suma])

    # Ordenar por:
    # 1) suma descendente
    # 2) nombre alfabético
    participantes.sort(key=lambda x: (-x[3], x[0]))

    # Determinar corte
    seleccionados = []

    if len(participantes) <= 10:
        seleccionados = participantes
    else:
        puntaje_corte = participantes[9][3]

        for p in participantes:
            if p[3] >= puntaje_corte:
                seleccionados.append(p)

    # Imprimir resultado
    for p in seleccionados:
        print(f"{p[0]};{p[1]};{p[2]};{p[3]}")


################################################

def dccshow():
    archivo = open("talentos.txt", "r")
    lineas = archivo.readlines()
    archivo.close()

    participantes = []

    for linea in lineas:
        datos = linea.strip().split(";")
        nombre, email, major = datos[0], datos[1], datos[2]
        suma = int(datos[3]) + int(datos[4]) + int(datos[5])
        participantes.append([nombre, email, major, suma])

    participantes.sort(key=lambda x: (-x[3], x[0]))

    if len(participantes) <= 10:
        seleccionados = participantes
    else:
        seleccionados = participantes[:10]
        puntaje_corte = seleccionados[-1][3]

        for p in participantes[10:]:
            if p[3] == puntaje_corte:
                seleccionados.append(p)
            else:
                break

    for p in seleccionados:
        print(f"{p[0]};{p[1]};{p[2]};{p[3]}")
