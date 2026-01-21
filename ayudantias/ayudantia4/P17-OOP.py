#usando A, B y C.

   def agrupar_atracciones(self):
        # Crear un grupo por cada atracción principal (en orden)
        grupos = []
        for principal in self.principales:
            grupos.append([principal])

        # Agrupar cada atracción secundaria con su principal más cercana
        for secundaria in self.secundarias:
            principal_cercana = self.principal_mas_cercana(secundaria)
            indice = self.principales.index(principal_cercana)
            grupos[indice].append(secundaria)

        return grupos

###########################

    def agrupar_atracciones(self):
        grupos = []
        principales_grupo = []

        # Crear un grupo por cada principal
        for principal in self.principales:
            grupos.append([principal])
            principales_grupo.append(principal)

        # Asignar secundarias al grupo correcto
        for secundaria in self.secundarias:
            principal_cercana = self.principal_mas_cercana(secundaria)

            for i in range(len(principales_grupo)):
                if principales_grupo[i] == principal_cercana:
                    grupos[i].append(secundaria)

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

            for grupo in grupos:
                if grupo[0] == principal_cercana:
                    grupo.append(secundaria)

        return grupos
    