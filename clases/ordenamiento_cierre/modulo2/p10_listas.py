def nivel_cancha(lista, altura):
    cantidad = 0
    for numero in lista:
        diferencia = abs(numero-altura)
        if diferencia>5:
            cantidad+=1
    return cantidad