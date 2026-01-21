def escribir_deliveries(p):
    p = p.lower()

    archivo_lectura = open("restaurantes.txt", "r", encoding="utf-8")
    archivo_escritura = open(f"{p}.txt", "w", encoding="utf-8")

    for linea in archivo_lectura:
        linea = linea.strip()

        if linea != "":
            partes = linea.split(";")
            nombre = partes[0]
            platos = partes[1].split("-")
            precios = partes[2].split("-")

            for i in range(len(platos)):
                if platos[i].lower() == p:
                    archivo_escritura.write(f"{nombre};{precios[i]}\n")

    archivo_lectura.close()
    archivo_escritura.close()


###################################

def escribir_deliveries(p):
    p = p.lower()

    with open("restaurantes.txt", "r", encoding="utf-8") as archivo_lectura, \
         open(f"{p}.txt", "w", encoding="utf-8") as archivo_escritura:

        for linea in archivo_lectura:
            linea = linea.strip()
            if linea == "":
                continue

            partes = linea.split(";")
            nombre = partes[0]
            platos = partes[1].split("-")
            precios = partes[2].split("-")

            for i in range(len(platos)):
                if platos[i].lower() == p:
                    archivo_escritura.write(f"{nombre};{precios[i]}\n")


############################

def escribir_deliveries(p):
    p = p.lower()

    with open("restaurantes.txt", "r", encoding="utf-8") as archivo_lectura, \
         open(f"{p}.txt", "w", encoding="utf-8") as archivo_escritura:

        for linea in archivo_lectura:
            linea = linea.strip()

            if linea != "":
                partes = linea.split(";")
                nombre = partes[0]
                platos = partes[1].split("-")
                precios = partes[2].split("-")

                for i in range(len(platos)):
                    if platos[i].lower() == p:
                        archivo_escritura.write(f"{nombre};{precios[i]}\n")

############################

def escribir_deliveries(p):
    p = p.lower()

    archivo_lectura = open("restaurantes.txt", "r", encoding="utf-8")
    lineas = archivo_lectura.readlines()
    archivo_lectura.close()

    archivo_escritura = open(f"{p}.txt", "w", encoding="utf-8")

    for linea in lineas:
        linea = linea.strip()

        if linea != "":
            partes = linea.split(";")
            nombre = partes[0]
            platos = partes[1].split("-")
            precios = partes[2].split("-")

            for i in range(len(platos)):
                if platos[i].lower() == p:
                    archivo_escritura.write(f"{nombre};{precios[i]}\n")

    archivo_escritura.close()
