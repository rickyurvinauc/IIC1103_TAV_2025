manejador_archivo = open("ejemplo.txt", 'r')
lista = manejador_archivo.readlines()
print(lista)
print(len(lista))

for linea in lista:
    print(linea)

for linea in lista:
    print(linea.strip())