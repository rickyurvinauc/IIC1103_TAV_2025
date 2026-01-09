def buscar_restaurantes(p):
    # Abre el archivo en modo lectura
    archivo = open('restaurantes.txt', 'r')
    # Lee todas las lineas del archivo y las guarda en una lista
    contenido = archivo.readlines()
    # Cierra el archivo despues de leerlo
    archivo.close()
    # Crea una lista vacia donde se guardaran los nombres que coincidan
    restaurantes = []
    # Recorre cada linea del archivo
    for linea in contenido:
        # Elimina los saltos de linea y separa los datos usando ';'
        datos = linea.strip().split(';')
        # Si el texto buscado (p) aparece dentro del nombre del restaurante
        if p in datos[0]:
            # Agrega el nombre del restaurante a la lista de resultados
            restaurantes.append(datos[0])
    # Devuelve la lista con todos los nombres que coincidieron
    return restaurantes