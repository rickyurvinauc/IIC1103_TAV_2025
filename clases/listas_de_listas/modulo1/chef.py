ingredientes_originales = ["pasta", "ensalada", "sopa"]
ayudante = ingredientes_originales
ayudante[0] = "pasta con salsa"
print("Receta original....")
print(ingredientes_originales)
print("Receta del ayudante....")
print(ayudante)
# Receta original....
# ['pasta con salsa', 'ensalada', 'sopa']
# Receta del ayudante....
# ['pasta con salsa', 'ensalada', 'sopa']

recetas = ["pasta", "ensalada", "sopa"]
ayudante = recetas.copy()
ayudante[0] = "pasta con pesto"
print("Receta original....")
print(recetas)
print("Receta del ayudante....")
print(ayudante)
# Receta original....
# ['pasta', 'ensalada', 'sopa']
# Receta del ayudante....
# ['pasta con pesto', 'ensalada', 'sopa']

recetario = [
    ["pasta", ["harina", "tomate"]],
    ["ensalada", ["lechuga", "tomate"]]
]
primer_ingrediente = recetario[0][1]
print(primer_ingrediente)
ayudante = recetario.copy()
ayudante[0][1][0] = "harina integral"
print("Receta original....")
print(recetario)
print("Receta del ayudante....")
print(ayudante)
# Receta original....
# [['pasta', ['harina integral', 'tomate']], ['ensalada', ['lechuga', 'tomate']]]
# Receta del ayudante....
# [['pasta', ['harina integral', 'tomate']], ['ensalada', ['lechuga', 'tomate']]]


import copy

recetario = [
    ["pasta", ["harina", "tomate"]],
    ["ensalada", ["lechuga", "tomate"]]
]
ayudante = copy.deepcopy(recetario)
ayudante[0][1][0] = "harina integral"
print("Recetario original:", recetario)
print("Recetario del ayudante:", ayudante)
# Recetario original: [['pasta', ['harina', 'tomate']], ['ensalada', ['lechuga', 'tomate']]]
# Recetario del ayudante: [['pasta', ['harina integral', 'tomate']], ['ensalada', ['lechuga', 'tomate']]]