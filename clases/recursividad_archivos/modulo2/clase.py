# Escribe un programa en Python que lea el 
# de notas.csv y cree un archivo .txt
# con todos los ruts de los estudiantes que tienen
# promedio mas de 580 en sus sets

#  el archivo debe llamarse como aprobados.txt
# 3-590
# 4-600

archivo_notas = open("notas.csv", "r")
contenido = archivo_notas.readlines()
archivo_notas.close()

archivo_nuevo = open("aprobados.txt", "a")
contenido = contenido[1:]

for nota in contenido:
    datos = nota.strip().split(",")
    puntajes = datos[2:]
    suma = 0
    for puntaje in puntajes:
        puntaje = int(puntaje)
        suma += puntaje
    promedio = suma / len(puntajes)
    if promedio > 580:
        texto = datos[0]+"-"+str(promedio)+"\n"
        archivo_nuevo.write(texto)
archivo_nuevo.close()