class Cabana:

    def __init__(self, numero, capacidad):
        self.numero = numero
        self.capacidad = capacidad
        self.ocupacion = 0

    def esta_vacia(self):
        if self.ocupacion == 0:
            return True
        else:
            return False

    def ocupar(self, numero):
        total_a_ocupar = numero + self.ocupacion

        if total_a_ocupar <= self.capacidad and self.esta_vacia() == True:
            self.ocupacion = total_a_ocupar
            return True

        return False

    def __str__(self):
        return f"{self.numero} ({self.ocupacion}/{self.capacidad})"