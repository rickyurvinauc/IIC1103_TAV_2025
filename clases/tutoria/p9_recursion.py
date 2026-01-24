# Escribe tu código aquí
from bingo import es_ganador

def  ganadores(tableros, ya_extraidos):
    # caso base
    if len(tableros) == 0:
        return 0
    cartor_1 = tableros[0]
    es_ganador_el_carton = es_ganador(cartor_1, ya_extraidos) # True o 
    if es_ganador_el_carton == True:
        return 1 + ganadores(tableros[1:], ya_extraidos)
    return ganadores(tableros[1:], ya_extraidos)


# pensemos la estrategia...
# primera llamada
#
# carton_1 = [[12,25,41,51,63],
#             [3,30,37,54,66],
#             [7,21,40,56,74],
#             [1,26,35,50,69],
#             [10,17,45,47,64]]
# return 1 + ganadores(tableros[1:])
# carton_2 = [[11,25,41,51,63],
#             [3,30,37,54,66],
#             [7,21,40,56,74],
#             [9,27,35,50,69],
#             [10,17,45,47,64]]

# segunda llamada

# carton_2 = [[11,25,41,51,63],
#             [3,30,37,54,66],
#             [7,21,40,56,74],
#             [9,27,35,50,69],
#             [10,17,45,47,64]]
# return ganadores([], ya_extraidos)

# # ultima llamda ( caso base)
# return 0
# # primera llamada
# return 1+ganadores(tableros, ya_extraidos) -> 1 + 0 -> 1
# # segunda llamada 
# return ganadores(tableros, ya_extraidos) -> 0
# # ultima llamada
# return 0

