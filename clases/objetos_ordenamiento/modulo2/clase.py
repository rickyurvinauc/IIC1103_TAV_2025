resultados = [
    ["Dora", 1200, 20],
    ["Bob", 950, 25],
    ["Homero", 1500, 45],
    ["Lisa", 1500, 60]
] # votos comuna San Joaquin

def criterio(item):
    return item[1], -item[2]

resultados.sort(key=criterio, reverse=True)

print(resultados)