class Estudiante:

    def __init__(self, nombre, carrera, edad):
        self.nombre = nombre
        self.carrera = carrera
        self.edad = edad
        self.cant_ramos_aprobados = 0

    def saludar(self):

        return f"Hola soy " +self.nombre +" y tengo "+ str(self.cant_ramos_aprobados) +" de ramos aprobados"
    
    def hacer_sentadilla(self):
        print("Estoy haciendo una sentadilla *********")

    def aprobar_curso(self):
        self.cant_ramos_aprobados += 1
    
isi = Estudiante("Isi","Ing. Civil", 19)
dilantero = Estudiante("Dilantero","Ing. Civil", 19)

print(dilantero.saludar())
isi.hacer_sentadilla()

isi.aprobar_curso()
dilantero.aprobar_curso()

print(isi.saludar())
print(dilantero.saludar())