class Pelicula:
    def __init__(self, nombre, anio, categoria, descripcion):
        self.nombre = nombre
        self.anio = anio
        self.categoria = categoria
        self.descripcion = descripcion
        self.puntos = []
        self.promedio = 0

    def __str__(self):
        return "La película: " + self.nombre + " del año: " \
        + str(self.anio) + " tiene un puntaje promedio de: " + str(self.promedio)

    def calcular_promedio(self):
        if self.puntos:
            suma = sum(self.puntos)
            self.promedio = round(suma / len(self.puntos), 1)
        else:
            self.promedio = 0
        
    def agregar_puntaje(self, puntaje):
        self.puntos.append(puntaje)
        self.calcular_promedio()
    
    def es_mejor_que(self, otra_pelicula):
        return self.promedio > otra_pelicula.promedio

p1 = Pelicula("Harry Potter 4", 2000, "Ficcion","Una pelicula de magia")
p1.agregar_puntaje(4)
p1.agregar_puntaje(5)
p1.agregar_puntaje(4)
p1.agregar_puntaje(3)

p2 = Pelicula("Harry Potter 3", 2001, "Ficcion","Una pelicula de magia")
p2.agregar_puntaje(1)
p2.agregar_puntaje(2)

print(p1.es_mejor_que(p2))

print(p1)