class Clasificador:
    def __init__(self):
        self.principales = []
        self.secundarias = []

    def agregar_atraccion(self, atraccion):
        if atraccion.principal:
            self.principales.append(atraccion)
        else:
            self.secundarias.append(atraccion)

    def principal_mas_cercana(self, atraccion):
        mas_cercana = self.principales[0]
        menor_distancia = atraccion.distancia(mas_cercana)

        for principal in self.principales:
            distancia_actual = atraccion.distancia(principal)
            if distancia_actual < menor_distancia:
                menor_distancia = distancia_actual
                mas_cercana = principal

        return mas_cercana

####################################################

    def principal_mas_cercana(self, atraccion):
        mas_cercana = None
        menor_distancia = None

        for principal in self.principales:
            distancia_actual = atraccion.distancia(principal)

            if menor_distancia is None or distancia_actual < menor_distancia:
                menor_distancia = distancia_actual
                mas_cercana = principal

        return mas_cercana
    
####################################################

    def principal_mas_cercana(self, atraccion):
        lista_distancias = []

        for principal in self.principales:
            distancia = atraccion.distancia(principal)
            lista_distancias.append((distancia, principal))

        return min(lista_distancias)[1]