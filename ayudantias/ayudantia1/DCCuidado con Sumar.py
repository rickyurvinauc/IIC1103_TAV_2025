suma = 0 # Variable para la suma de numeros positivos
negativos_pendientes = 0 # Contador de negativos pendientes de procesar

# Leer numeros hasta que se ingrese un 0
while True:
    # Leer el numero
    n = int(input())
    # Si el numero es 0, terminar el proceso
    if n == 0:
        #imprimir FIN y salir del ciclo
        print("FIN")
        break
    # Si hay negativos pendientes por procesar
    if negativos_pendientes > 0:
        # No sumar positivos mientras haya negativos pendientes
        print(f"NO SUMA {n}")
        # Si el numero es negativo, decrementar el contador de negativos pendientes
        if n < 0:
            # Decrementar el contador de negativos pendientes
            negativos_pendientes -= 1
    else:
        # Si no hay negativos pendientes, procesar el numero
        if n < 0:
            # Si el numero es negativo, no sumar y aumentar el contador de negativos pendientes
            print(f"NO SUMA {n}")
            negativos_pendientes = -n
        else:
            # Si el numero es positivo, sumar a la suma total
            print(f"SI SUMA {n}")
            suma += n
# Imprimir la suma total de numeros positivos

print(suma)
