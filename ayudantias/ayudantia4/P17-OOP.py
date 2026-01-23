#usando partes anteriores del ejercicio p15 y p16
   def agrupar_atracciones(self):
        # Crear un grupo por cada atracción principal (en orden)
        grupos = []
        # Recorrer las atracciones principales
        for principal in self.principales:
            # agregar a la lista grupos una lista que contiene solo la atracción principal de la iteracion
            grupos.append([principal])
        # grupos = [[principal1], [principal2], ..., [principalN]]

        # Agrupar cada atracción secundaria con su principal más cercana
        # recorrer las atracciones secundarias
        for secundaria in self.secundarias:
            # para cada secundaria, buscar su principal mas cercana
            principal_cercana = self.principal_mas_cercana(secundaria)
            # encontrar el indice de la principal mas cercana en la lista de principales
            # metodo index de listas lista.index(elemento) devuelve el indice de la primera aparicion de elemento en lista
            indice = self.principales.index(principal_cercana)
            # agregar la secundaria al grupo correspondiente
            # con indice voy a la lista que tiene la atraccion principal en ese indice dentro de la lista grupos que tiene N listas de las N atracciones principales
            grupos[indice].append(secundaria)
            # por ej si indice es 0, grupos[0] que eso es [principal1], le agrego la secundaria mas cercana a principal1
        # retornar grupos formados con una atraccion principal cada uno y 0 o mas atracciones secundarias asociadas
        return grupos

###########################

    def agrupar_atracciones(self):
        #inicializar listas vacias
        grupos = []
        principales_grupo = []

        # Crear un grupo por cada atraccion principal
        for principal in self.principales:
            # agregar a la lista grupos una lista que contiene solo la atracción principal de la iteracion
            grupos.append([principal])
            # agregar la principal a la lista de principales del grupo
            principales_grupo.append(principal)

        # Asignar secundarias al grupo correcto
        for secundaria in self.secundarias:
            # obtener la principal mas cercana a la secundaria actual
            principal_cercana = self.principal_mas_cercana(secundaria)

            # buscar el indice de la principal mas cercana en la lista de principales del grupo
            for i in range(len(principales_grupo)):
                # si el elemento en la posicion i de la lista principales_grupo es igual a la principal mas cercana
                if principales_grupo[i] == principal_cercana:
                    # agregar la secundaria al grupo correspondiente
                    grupos[i].append(secundaria)
        # retornar grupos formados
        return grupos

#############################

    def agrupar_atracciones(self):
        grupos = []

        # Crear los grupos con solo las principales
        for principal in self.principales:
            grupos.append([principal])

        # Para cada secundaria, buscar su grupo
        for secundaria in self.secundarias:
            principal_cercana = self.principal_mas_cercana(secundaria)

            # por cada grupo en la lista grupos que tiene listas de atracciones
            for grupo in grupos:
                # si la primera atraccion del grupo (que es la principal) es igual a la principal mas cercana
                if grupo[0] == principal_cercana:
                    # agregar la secundaria al grupo
                    grupo.append(secundaria)

        return grupos
    