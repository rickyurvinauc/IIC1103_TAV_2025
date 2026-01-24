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
        # recibe de parametro un objeto de la clase Atraccion, esta en variable atraccion
        mas_cercana = self.principales[0]
        # Inicializo la menor distancia con la distancia a la primera atraccion principal
        ## funcion distancia la entregan en enunciado
        menor_distancia = atraccion.distancia(mas_cercana)
        # Recorro las atracciones principales
        for principal in self.principales:
            # Calculo la distancia a la atraccion principal actual
            distancia_actual = atraccion.distancia(principal)
            # Si la distancia actual es menor a la menor distancia registrada
            if distancia_actual < menor_distancia: 
                # reemplazamos la atraccion mas cercana y la menor distancia
                menor_distancia = distancia_actual # actualizo menor distancia
                mas_cercana = principal #actualizo la atraccion mas cercana por principal, que es la de la iteracion actual
        #retorno la atraccion principal mas cercana
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
        # lista con distancias, comienza vacia
        lista_distancias = []
        # recorro las atracciones principales
        for principal in self.principales:
            #calculo la distancia entre la atraccion dada y la principal actual
            distancia = atraccion.distancia(principal)
            # agrego una tupla (distancia, principal) a la lista
            lista_distancias.append([distancia, principal])

        return min(lista_distancias)[1]