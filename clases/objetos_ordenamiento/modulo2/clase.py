class Canditato:

    def __init__(self, nombre, votos, edad):
        self.nombre = nombre
        self.votos = votos
        self.edad = edad
    
    def __str__(self):
        return f"El candidato {self.nombre} tiene: {self.votos}"
        
c1 = Canditato("Homero", 1500, 50) # nombre -> homero, votos -> 1500, edad -> 50
c2 = Canditato("Lisa", 2800, 50)
c3 = Canditato("Harry Potrer", 700, 50)
print(c2)

print(c1.votos)
lista = [
    c1, 
    c2, 
    c3
    ]

def criterio_votos(pepito):
    # canditato -> c1, c2, c2
    return -pepito.votos, pepito.edad

lista.sort(key=criterio_votos)

for c in lista:
    print(c)

lista_candidatos = [
    ["Homero", 1500, 50],
    ["Lisa", 2800, 50],
    ["Harry Potrer", 700, 50],
]

def criterio_lista(sublista):
    #sublista ->   ["Homero", 1500, 50],
    return sublista[1]

lista_candidatos.sort(key=criterio_lista)
