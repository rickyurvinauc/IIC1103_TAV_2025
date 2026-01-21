def buscar_restaurantes(p):
    resultado = []
    p = p.lower()

    with open("restaurantes.txt", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if linea == "":
                continue

            nombre_restaurante = linea.split(";")[0]

            if p in nombre_restaurante.lower():
                resultado.append(nombre_restaurante)

    return resultado


###########################

def buscar_restaurantes(p):
    resultado = []
    p = p.lower()

    archivo = open("restaurantes.txt", "r", encoding="utf-8")

    for linea in archivo:
        linea = linea.strip()
        if linea == "":
            continue

        nombre_restaurante = linea.split(";")[0]

        if p in nombre_restaurante.lower():
            resultado.append(nombre_restaurante)

    archivo.close()
    return resultado

############################
def buscar_restaurantes(p):
    resultado = []
    p = p.lower()

    with open("restaurantes.txt", "r", encoding="utf-8") as archivo:
        linea = archivo.readline()
        while linea != "":
            linea = linea.strip()
            if linea != "":
                nombre_restaurante = linea.split(";")[0]
                if p in nombre_restaurante.lower():
                    resultado.append(nombre_restaurante)
            linea = archivo.readline()

    return resultado


################################


def buscar_restaurantes(p):
    resultado = []
    p = p.lower()

    with open("restaurantes.txt", "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

    for linea in lineas:
        linea = linea.strip()
        if linea == "":
            continue

        nombre_restaurante = linea.split(";")[0]

        if p in nombre_restaurante.lower():
            resultado.append(nombre_restaurante)

    return resultado
