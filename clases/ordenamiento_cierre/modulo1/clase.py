
candidatos = [
    ["Homero", 1600, 35],
    ["Lisa", 800, 65],
    ["Harry Potter", 2500, 22],
]

def criterio(item):
    # item ->  ["Homero", 1600, 35]
    return item[1]

candidatos.sort(key=criterio, reverse=True)

for c in candidatos:
    print(c)