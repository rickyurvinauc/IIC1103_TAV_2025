# Abrir el archivo para escritura (sobrescribe si ya existe)
archivo = open('notas_2.csv', 'w')

# Preparar la cabecera como una unica linea CSV
# Evitar escribir la cabecera dos veces: basta una sola llamada a write
cabecera = 'N Alumno,Nota Final,Set 1,Set 2,Set 3,Set 4,Set 5\n'
# Escribir la cabecera en el archivo
archivo.write(cabecera)
# o se puede escribir con writelines
# archivo.writelines([cabecera])

# Preparar las filas de datos como listas de valores numericos
# Cada sublista representa una fila que luego convertiremos a cadena CSV
notas = []
notas.append([1, 5, 600, 600, 600, 600, 600])
notas.append([2, 4, 600, 600, 600, 600, 600])
notas.append([3, 4, 600, 600, 600, 600, 600])
notas.append([4, 3, 600, 200, 450, 600, 96])
notas.append([5, 3, 600, 600, 300, 340, 0])

# Recorrer cada fila y construir la linea CSV manualmente
# Se convierte cada valor a string y se separa por comas
for fila in notas:
    # Iniciar la cadena de la fila vacia
    fila_cadena = ''
    # Recorrer los elementos por indice para poder controlar la coma entre campos
    i = 0
    while i < len(fila):
        valor = fila[i]
        celda = str(valor)  # convertir el valor a texto para escribirlo
        if i == 0:
            # para el primer campo no anteponer coma
            fila_cadena = celda
        else:
            # para los siguientes campos, anteponer una coma
            fila_cadena = fila_cadena + ',' + celda
        i = i + 1
    # Escribir la linea completa y añadir salto de linea al final
    archivo.write(fila_cadena + '\n')

# Cerrar el archivo de forma explicita para liberar recursos
archivo.close()

# Mensaje simple de confirmacion (no forma parte del archivo)
print('Se escribieron', len(notas), 'filas en el archivo notas_2.csv')
