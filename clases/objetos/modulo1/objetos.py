class Persona:

    def __init__(self, nombre, apellido, rut, edad, ramos):
        self.nombre = nombre
        self.apellido = apellido
        self.rut = rut
        self.edad = edad
        self.ramos = ramos
    
    def __str__(self):
        return "Hola soy" + self.nombre +" y tengo "+str(self.edad)+" anios"

    def saludar(self):
        return "Hola a todas y todos soy: "+self.nombre
    
    def calcular_anio_nacimiento(self, anio_actual):
        resultado =  anio_actual - self.edad
        return resultado

mati = Persona("Mati","Calderon","29999999",19,["Intro","Mate","Fisica"])
ricardo = Persona("Ricardo","Urvina","288888",29,["Intro","Estadistica"])
print(mati)
print(ricardo)

