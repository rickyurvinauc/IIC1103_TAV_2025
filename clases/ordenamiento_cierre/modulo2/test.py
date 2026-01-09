class Estudiante:

    def __init__(self, nombre, rut):
        self.nombre = nombre
        self.rut = rut
        self.estado = False
    
    def cambiar_estado(self):
        self.estado = True
    
    def __str__(self):
        return f"Hola soy {self.nombre}"


class Curso:

    def __init__(self):
        self.estudiantes = []
    
    def inscribir_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
    
    def __str__(self):
        return f"El curso tiene {len(self.estudiantes)} estudiantes"

e1 = Estudiante("Fernanda","2777777")
e2 = Estudiante("Ricardo", "28888888")
e3 = Estudiante("Ingrid","26666666")
c1 = Curso()
c1.inscribir_estudiante(e3)
c1.inscribir_estudiante(e1)
c1.inscribir_estudiante(e2)
e3.cambiar_estado()

# crea una funcion que reciba un curso y guarde en un archivo los nombres de los estudiantes que aprobaron

def guardar_aprobados(curso):
    archivo = open("aprobados.txt", "a")
    for estudiante in curso.estudiantes:
        if estudiante.estado:
            texto = f"{estudiante.nombre}\n"
            archivo.write(texto)
    archivo.close()



guardar_aprobados(c1)

    



