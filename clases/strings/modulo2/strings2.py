# Slice con 3 argumentos

cadena = "Viva Chile"

subcadena = cadena[1:6:2]
print(subcadena)

subcadena = cadena[::2]
print(subcadena)

subcadena = cadena[1::2]
print(subcadena)

# Contar ocurrencias
print("ocurrencias")
cantidad = cadena.count("i")
print(cantidad)#2

cantidad = cadena.count("i", 2)
print(cantidad)#1

cantidad = cadena.count("i", 2, 6)
print(cantidad)#0

# Buscar el primer indice donde aparece una subcadena
print("indices")
indice = cadena.find("i")
print(indice) #1
indice = cadena.find("Ch",2,6)
print(indice) # -1

#Convertir a mayusculas y minusculas

cadena_minusculas = cadena.lower()
print(cadena_minusculas) # viva chile

cadena_mayusculas = cadena.upper()
print(cadena_mayusculas) #VIVA CHILE

#consultar si es mayuscula o minuscula
es_mayuscula_cadena = cadena.isupper()
print(es_mayuscula_cadena) #False

es_minuscula_cadena = cadena.islower()
print(es_minuscula_cadena) #es_minuscula_cadena
#todos los caracteres tienen que ser mayusculas o minusculas para que se retorne True

cadena_con_espacios = "  Viva Chile  "
cadena_sin_espacios_izquierda = cadena_con_espacios.lstrip()
print(cadena_sin_espacios_izquierda) #"Viva Chile.  "

cadena_sin_espacios_derecha = cadena_con_espacios.rstrip()
print(cadena_sin_espacios_derecha) #"  Viva Chile."

cadena_sin_espacios = cadena.strip()
print(cadena_sin_espacios) #"Viva Chile"

#remplazar en un texto
nombre = "Hola Ricky"
remplazo = nombre.replace("Ricky", "Ingrid")
print(remplazo) #Hola Ingrid
