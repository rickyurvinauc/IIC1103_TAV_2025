# Escribe tu código aquí!
class Planta:

    def __init__(self, nombre, resistencia):
        self.nombre = nombre
        self.resistencia = resistencia # 10
        self.agua = 0

    def __str__(self):
        # varias lineas de codigo
        # validaciones o cualquiera cosa
        # pero SIEMPRE debe retornar un string
        return f"{self.nombre} - {self.agua}/{self.resistencia}"
    
    def regar(self, agua): # agua -> 13
        peso_total = agua + self.agua

        if peso_total <= self.resistencia:
            self.agua += agua
        else:
            self.agua = self.resistencia

