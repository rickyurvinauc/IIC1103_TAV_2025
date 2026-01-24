# Escribe tu código aquí

archivo = open("talentos.txt","r")
contenido = archivo.readlines()
archivo.close()
resultado = []
lista_majors = []
for linea in contenido:
    # linea ->"Alex;alex88@abalon.org;Fisica;30;65;14\n"
    datos = linea.strip().split(";")
    # datos -> ["Pedro","pedro59@musica.org";"Musica";"57";"61";"45"]
    nombre = datos[0]
    correo = datos[1]
    major = datos[2]
    archivo = open(major+".txt","a") # a -> append, no sobre escribe y escribe al ultimo
    texto = nombre + ";"+correo+"\n"
    # archivo.write(texto)
    print(f"{nombre};{correo}", file=archivo)
    archivo.close()

