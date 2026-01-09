def leer_archivos():
    # Abrir el archivo 'ramos.csv' en modo lectura
    ramos = open('ramos.csv', 'r')
    # Leer todas las lineas del archivo en una lista
    contenido_ramos = ramos.readlines()
    # Cerrar el archivo para liberar recursos
    ramos.close()

    # Lista donde se guardaran los ruts (identificadores) asociados al ramo buscado
    lista_ruts = []
    # Recorrer cada linea del archivo de ramos
    for ramo in contenido_ramos:
        # Quitar espacios y saltos de linea, y luego separar por coma
        datos = ramo.strip().split(',')
        # Si la linea corresponde al ramo 'IIC1103', guardar el rut (campo 0)
        if 'IIC1103' in ramo:
            lista_ruts.append(datos[0])

    estudiantes = open('estudiantes.csv', 'r')
    contenido = estudiantes.readlines()
    estudiantes.close()
    # Lista donde se guardaran los datos completos de los estudiantes filtrados
    lista_estudiantes = []
    # Recorrer cada linea del archivo de estudiantes
    for estudiante in contenido:
        # Quitar espacios y saltos de linea, y separar por coma para obtener campos
        datos = estudiante.strip().split(',')
        # El primer campo es el rut del estudiante
        rut = datos[0]
        # Si el rut esta en la lista de ruts del ramo, anadir la fila completa a la lista
        if rut in lista_ruts:
            lista_estudiantes.append(datos)

    return lista_estudiantes
