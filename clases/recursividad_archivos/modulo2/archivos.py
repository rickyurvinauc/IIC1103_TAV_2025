# python
# Ejemplo paso a paso usando solo open() y close()
# Archivo utilizado: `archivo1.txt`

# 1) LECTURA: abrir el archivo, usar readlines() y cerrar siempre
# abrir en modo lectura
archivo = open("archivo1.txt", "r")
print("Abierto `archivo1.txt` en modo 'r'")

# readlines() devuelve una lista de cadenas; se guarda en la variable 'contenido'
contenido = archivo.readlines()
print("Tipo devuelto por readlines():", type(contenido))
print("Contenido:")
for linea in contenido:
    # repr() muestra caracteres especiales como '\n'
    print(linea.strip()) # strip elimina espacios y saltos de linea al imprimir

# explicacion breve de '\n'
print("Nota: ' \n' es el caracter de nueva linea. Si una linea termina con ' \n', aparecera al final de la cadena.")

# cerrar el archivo manualmente
archivo.close()
print("Archivo cerrado con archivo.close()\n")

# 2) ESCRITURA con modo 'w' (sobrescribe o crea el archivo)
print("Modo 'w': sobrescribe el archivo o lo crea si no existe.")

# usar write() para escribir una cadena (sobrescribe contenido previo)
archivo = open("archivo1.txt", "w")
archivo.write("Noche de Halloween - primera linea \n")  # incluir '\n' para terminar linea
archivo.close()
print("Se escribio una linea con write() y se cerro el archivo.")

# usar writelines(): recibe un iterable de cadenas. NO anade '\n' automaticamente
lineas_para_escribir = [
    "Noche de Halloween \n",
    "Casa embrujada \n",
    "Calabazas y velas \n"
]
archivo = open("archivo1.txt", "w")
archivo.writelines(lineas_para_escribir)  # cada elemento debe incluir su propio '\n' si se quiere linea separada
archivo.close()
print("Se escribieron varias lineas con writelines() y se cerro el archivo.")

# leer para comprobar el contenido tras 'w'
archivo = open("archivo1.txt", "r")
print(" \nContenido despues de modo 'w':")
print(archivo.read())
archivo.close()

# 3) APPEND con modo 'a' (aniade al final sin borrar lo existente)
print(" \nModo 'a': anade texto al final del archivo sin borrar el contenido anterior.")

archivo = open("archivo1.txt", "a")
archivo.write("Dulces o travesuras \n")
archivo.close()
print("Se anadio una linea con write() en modo 'a' y se cerro el archivo.")

archivo = open("archivo1.txt", "a")
archivo.writelines(["Fantasmas en la noche \n", "Luces y sombras \n"])
archivo.close()
print("Se anadieron varias lineas con writelines() en modo 'a' y se cerro el archivo.")

# lectura final para mostrar el resultado
archivo = open("archivo1.txt", "r")
print(" \nContenido final del archivo:")
print(archivo.read())
archivo.close()

# Resumen:
# - Para leer lineas como lista: usar readlines() -> lista guardada en 'contenido'.
# - '\n' es el separador de linea dentro de las cadenas.
# - Siempre cerrar archivos: usar archivo.close() .
# - 'w' sobrescribe (write + writelines), 'a' anade al final (append).
