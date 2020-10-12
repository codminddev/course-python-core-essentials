# Polimorfismo
import math

class Figura:
    def perimetro(self):
        print("Mostrando perimetro")

    def area(self):
        print("Mostrando área")

class Rectangulo(Figura):
    def __init__(self, largo, alto):
        self.largo = largo 
        self.alto = alto
    
    def perimetro(self):
        perimetro = self.largo + self.largo + self.alto + self.alto
        print("El perimetro es", perimetro)
    
    def area(self):
        area = self.largo * self.alto
        print("El area es ", area)
    
class Circulo(Figura):
    
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        area = 3.1614 * self.radio ** 2
        print("El área es", area)

    def perimetro(self):
        perimetro = 2 * math.pi * self.radio
        print("El perimetro es", perimetro)

rectangulo = Rectangulo(2 , 3)
rectangulo.area()
rectangulo.perimetro() 

circulo  = Circulo(3)
circulo.area()
circulo.perimetro()

fig: Figura

for fig in [ Circulo(4), Circulo(6), Circulo(2), Rectangulo(3,2), Rectangulo(6,3)]:
    fig.area()
    fig.perimetro()