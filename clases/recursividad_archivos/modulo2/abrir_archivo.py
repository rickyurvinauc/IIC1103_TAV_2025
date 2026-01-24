# manejador_archivo = open('ejemplo.txt', 'r')
# # print(manejador_archivo)
# lista = manejador_archivo.readlines()

# for linea in lista:
#     print(linea)


# FileNotFoundError: [Errno 2] No such file or directory: 'ejemplo2.txt'
# <_io.TextIOWrapper name='ejemplo.txt' mode='r' encoding='UTF-8'>
pepito = open("ejemplo456.txt","a")
pepito.write("Hola\n")
pepito.write("Mundo\n")
pepito.close()


# archivo = open("ejemplo.txt","w") 
# # w -> sobreescribia
# # a  -> append


# lista3 =[
#     "HOLA MUNDO 2..\n",
#     "SOY RICARDO OTRA VEZ...\n"
# ]
# lista = primeras_tres + lista3 + ultimas
# archivo.writelines(lista) # recibe una lista de strings

# print(archivo)
# archivo.close() # SUPER IMPORTANTE