# No cambiar el nombre de la función
# def fallado(7223, 3)
def fallado(n, ultimo):
    # Escribe tu codigo aqui
    # caso baso
    n = str(n)  # n -> "7223"
    if len(n) == 1: # caso base...
        return -1
    
    ultimo = n[-1] # [-1] obtiene el ultimo elemento sea de un string o de una lista..
    penultimo = n[-2]
    if ultimo == penultimo:
        return ultimo

    return fallado(n[0:len(n)-1], ultimo)


# pensar mi estrategia..
# yo al menos me siento mas comodo trabajando con strings que con numeros..
# mi problema grande es el n -> 7223
# ultimo = 3
# penultimo = = 2
# si son iguales retorno cualquiera de los dos y se acaba....
# sino, voy a eliminar el ultimo  n -> 722
# ultimo = 2
# penultimo = = 2
# como son iguales retorno el 2

# cuando no falla "723"
# ultimo = 3
# penultimo = 2
# borro el ultimo n -> "72"
# ultimo = 2
# penultimo = 7
# borro el ultimo "7" -> que no falla entonces retorno -1 (caso base...)