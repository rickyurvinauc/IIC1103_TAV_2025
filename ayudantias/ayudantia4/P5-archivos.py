def buscar_restaurantes(p):
    # inicializar lista de resultados
    resultado = []
    # convertir p a minusculas
    p = p.lower()
    # abrir el archivo usando with modo lectura y encoding utf-8
    with open("restaurantes.txt", "r", encoding="utf-8") as archivo:
        # recorrer cada linea del archivo
        for linea in archivo:
            # limpiar linea de espacios en blanco
            linea = linea.strip()
            # si la linea esta vacia, continuar al siguiente ciclo
            if linea == "":
                continue
            # obtener el nombre del restaurante (antes del primer ";")
            nombre_restaurante = linea.split(";")[0]
            # si p esta en el nombre del restaurante (en minusculas)
            if p in nombre_restaurante.lower():
                # agregar el nombre del restaurante a la lista de resultados
                resultado.append(nombre_restaurante)
    # retorno la lista de resultados
    return resultado


###########################

def buscar_restaurantes(p):
    resultado = []
    p = p.lower()

    # abrir archivo modo lectura con open
    archivo = open("restaurantes.txt", "r", encoding="utf-8")

    # recorrer cada linea del archivo
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
