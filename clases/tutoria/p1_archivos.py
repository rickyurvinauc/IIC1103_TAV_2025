# Escribe tu código aquí

major = input() # Fisica

archivo = open("talentos.txt","r")
contenido = archivo.readlines() 
# contenido 
# [
# 'Pedro;pedro59@musica.org;Musica;57;61;45\n'
# 'Leo;leo58@uni-uni.dev;Fisica;31;44;34\n'
# 'Naomi;naomi55@avalon.org;Artes;48;68;25\n'
# 'Alex;alex88@abalon.org;Fisica;30;65;14\n'
# 'Martin;martin67@robotica-tech.net;Ingenieria;43;22;33\n'
# ]
contador = 0

for linea in contenido:
    #linea = 'Leo;leo58@uni-uni.dev;Fisica;31;44;34\n'
    #linea = 'Leo;leo58@uni-uni.dev;Fisica;31;44;34'
    datos = linea.strip().split(";")
    # datos = ["Leo","leo58@uni-uni.dev","Fisica","44","34"]
    if major == datos[2]: # "Histora" == "Historia de Chile"
        contador += 1

print(contador)

# recordemos...
# cadena_a = "abc"
# cadena_b = "ba"

# print(cadena_b in cadena_a)