class Persona:

    def __init__(self, nombre, edad, RUT_PERSONA): # parametros que necesita la clase para crear un objeto
        self.nombre = nombre
        self.edad = edad
        self.rut = RUT_PERSONA
    
    def saludar(self):
        print("Hola soy " + self.nombre + "  y tengo: "+str(self.edad))
        return "Hola soy " + self.nombre + "  y tengo: "+str(self.edad)

    def __str__(self):
        if self.edad > 18:
            return "Hola soy " + self.nombre + "  y soy mayor de edad"
        else:
            return "Hola soy " + self.nombre + "  y soy menor de edad"

vicente = Persona("Vicho", 21, 2800000)
ricardo = Persona("Ricardo", 16, 2900000)
ingrid = Persona("Ingrid", 30, 2900000)

print(type(vicente))

x = 10
print(type(x))