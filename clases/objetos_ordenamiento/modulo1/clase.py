class Estudiante:

    def __init__(self, nombre):
        self.nombre = nombre

class Curso:

    def __init__(self):
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):

        for est in self.estudiantes:
            if est.nombre == estudiante.nombre:
                return "El estudiante ya existe"
        
        self.estudiantes.append(estudiante)
        return "Estudiante creado exitosamente"


curso = Curso()
curso2 = Curso()

curso.agregar_estudiante(e1)
curso.agregar_estudiante(e2)
curso.agregar_estudiante(e3)


e1 = Estudiante("Juan")
e2 = Estudiante("Pepito")
e3 = Estudiante("Roberto")



e4 = Estudiante("Pepito")
curso.agregar_estudiante(e4)
