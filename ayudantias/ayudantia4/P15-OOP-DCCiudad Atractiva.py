class Clasificador:
    def __init__(self):
        self.principales = []
        self.secundarias = []

    def agregar_atraccion(self, atraccion):
        if atraccion.principal:
            self.principales.append(atraccion)
        else:
            self.secundarias.append(atraccion)
