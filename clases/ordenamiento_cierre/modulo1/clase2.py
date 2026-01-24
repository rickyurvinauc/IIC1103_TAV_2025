

class Candidato:

    def __init__(self, nombre, votos, edad):
        self.nombre = nombre
        self.votos = votos
        self.edad = edad
    
    def __str__(self):
        return f"El candidato {self.nombre} tiene {self.votos}"


homero = Candidato("Homero", 1600, 35)
lisa = Candidato("Lisa", 800, 35)
harryp = Candidato("Harry Potter", 2500, 22)

lista = [homero, lisa, harryp]
def criterio(candidato):
    # item -> Candidato

    return candidato.votos
lista.sort(key=criterio, reverse=True)

for c in lista:
    print(c)
        