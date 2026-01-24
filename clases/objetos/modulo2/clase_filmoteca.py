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

    def agregar_puntuacion(self, puntaje):
        self.puntos.append(puntaje)
        self.calcular_promedio()

    def es_mejor_que(self, otra_pelicula):
        return self.promedio > otra_pelicula.promedio

class Filmoteca:
    def __init__(self):
        self.peliculas = []

    def __str__(self):
        return "Filmoteca con " + str(len(self.peliculas)) + " películas"

    def agregar_pelicula(self, pelicula): # agrega la pelicula si no existe en la lista
        encontrada = False
        for peli in self.peliculas:
            if peli.nombre == pelicula.nombre:
                encontrada = True
        
        if encontrada == False:
            self.peliculas.append(pelicula)


    def contar_por_anio(self):
        conteo = []
        for pelicula in self.peliculas:
            encontrado = False
            for item in conteo:
                if item[0] == pelicula.anio:
                    item[1] += 1
                    encontrado = True
                    break
            if not encontrado:
                conteo.append([pelicula.anio, 1])
        return conteo

    def mejor_pelicula(self):
        if not self.peliculas:
            return None
        mejor = self.peliculas[0]
        for indice_p in range(1,len(self.peliculas)):
            pelicula = self.peliculas[indice_p]
            if pelicula.es_mejor_que(mejor):
                mejor = pelicula
        return mejor


pelicula1 = Pelicula("Una nueva esperanza", 1997, "Ciencia ficcion", "Un joven granjero intercepta una llamada de socorro")
pelicula2 = Pelicula("La amenaza fantasma", 2017, "Ciencia ficcion", "Los Jedi descubren a Anakin Skylwalker")
pelicula3 = Pelicula("Dunkirk", 2017, "Guerra", "Dramatica evacuacion de Dunkirk durante la Segunda Guerra Mundial")

pelicula1.agregar_puntuacion(8)
pelicula1.agregar_puntuacion(9)
pelicula2.agregar_puntuacion(9)
pelicula2.agregar_puntuacion(10)
pelicula3.agregar_puntuacion(7)
pelicula3.agregar_puntuacion(8)

filmoteca = Filmoteca()
filmoteca.agregar_pelicula(pelicula1)
filmoteca.agregar_pelicula(pelicula2)
filmoteca.agregar_pelicula(pelicula3)

print(filmoteca)
print("Conteo por año:", filmoteca.contar_por_anio())
print("Mejor pelicula:", filmoteca.mejor_pelicula())

print("¿Es 'Una nueva esperanza' mejor que 'La amenaza fantasma'?:", pelicula2.es_mejor_que(pelicula1))
print("¿Es 'Dunkirk' mejor que 'La amenaza fantasma'?:", pelicula3.es_mejor_que(pelicula2))