def validez_fila(numeros, total):

    if len(numeros) == 0:
        return 0
        
    numero = numeros[0]
    suma = numero + validez_fila(numeros[1:], total)

    if suma == total and len(numeros) == 0:
        return True
    elif len(numeros) == 0 and suma != total:
        return False
    

fila = [12, 1, 3, 1, 2, 5]
total = fila[0]
numeros = fila[1:]
print(validez_fila(numeros, total))