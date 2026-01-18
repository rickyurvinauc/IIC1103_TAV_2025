suma = 0 # Variable para la suma de numeros positivos
negativos_pendientes = 0 # Contador de negativos pendientes de procesar

# Leer numeros hasta que se ingrese un 0
while n!= 0:
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
# si salí del ciclo es porque n = 0. En ese caso debo imprimir "FIN"
print("FIN")
# Imprimir la suma total de numeros positivos
print(suma)
