class Equipo:

    def __init__(self, nombre):
        self.nombre = nombre
        self.jugadores = []
        self.puntos = 0

    def agregar(self, jugador):
        self.jugadores.append(jugador)

    def enfrentar(self, rival):

        for i in range(len(rival.jugadores)):
            j1 = self.jugadores[i]
            j2 = rival.jugadores[i]
            if j1.nivel > j2.nivel:
                self.puntos += 1
            elif j1.nivel < j2.nivel:
                rival.puntos += 1

        if self.puntos > rival.puntos:
            return self.nombre
        elif self.puntos < rival.puntos:
            return rival.nombre
        else:
            return "Empate"