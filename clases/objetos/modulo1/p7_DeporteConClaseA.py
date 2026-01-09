class Jugador:

    def __init__(self, nombre,tipo, nivel=0):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo

    def entrena(self, horas):
        if self.tipo == 'esforzado':
            self.nivel += int(horas/24)
        elif self.tipo == 'talentoso':
            self.nivel += int(horas/4)

    def __str__(self):
        return "El jugador "+self.nombre+" posee un nivel de "+str(self.nivel)