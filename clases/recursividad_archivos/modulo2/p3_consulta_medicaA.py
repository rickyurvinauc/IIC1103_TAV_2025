# Abre el archivo llamado 'examen.txt' en modo lectura ('r')
archivo = open('examen.txt', 'r')
# Lee todas las lineas del archivo y las guarda en una lista
contenido = archivo.readlines()
# Cierra el archivo despues de leerlo
archivo.close()
# Recorre cada linea del archivo
for linea in contenido:
    # Elimina los saltos de linea y separa los datos por punto y coma
    datos = linea.strip().split(';')
    # Convierte los valores numericos del texto a tipo float
    valor = float(datos[1])
    lim_i = float(datos[2])
    lim_s = float(datos[3])
    # Si el valor esta por debajo del limite inferior, imprime el nombre con un signo negativo
    if valor < lim_i:
        print(datos[0] + " -")
    # Si el valor esta por encima del limite superior, imprime el nombre con un signo positivo
    elif valor > lim_s:
        print(datos[0] + " +")