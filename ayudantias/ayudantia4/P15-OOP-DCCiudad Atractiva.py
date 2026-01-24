class Clasificador:
    # constructor
    def __init__(self):
        self.principales = []
        self.secundarias = []

    def agregar_atraccion(self, atraccion):
        # recibe de parametro un objeto de la clase Atraccion, esta en variable atraccion
        if atraccion.principal == True:
            self.principales.append(atraccion)
        else:
            self.secundarias.append(atraccion)
