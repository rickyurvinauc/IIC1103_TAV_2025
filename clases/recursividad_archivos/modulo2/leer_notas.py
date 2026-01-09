# python
# Abrir el archivo 'notas.csv' en modo lectura
archivo = open('notas.csv', 'r', encoding='utf-8')

# Leer todas las lineas del archivo y guardarlas en una lista
contenido = archivo.readlines()

# La primera linea contiene la cabecera: quitar espacios y separar por comas
cabecera = contenido[0].strip().split(',')

# El resto de las lineas son las filas de datos
notas = contenido[1:]

# Cerrar el archivo de forma explicita para liberar recursos
archivo.close()

# Mostrar el contenido crudo para que el alumno vea el formato del archivo
print(contenido)

# Mostrar la cabecera ya procesada como lista de nombres de columna
print(cabecera)

# Recorrer cada linea de datos, limpiarla y dividirla en campos
for linea in notas:
    # Quitar espacios al inicio y al final de la linea
    linea_limpia = linea.strip()
    # Dividir la linea por la coma para obtener los campos de la fila
    campos = linea_limpia.split(',')
    # Imprimir la lista de campos de la fila actual
    print(campos)