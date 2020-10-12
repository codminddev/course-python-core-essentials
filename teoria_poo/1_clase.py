class Perro:    
    def ladrar(self):
        print( self.nombre + " está landrando woff woff...")
    
    def dormir(self):
        print(f"El perro color {self.color_pelo} con ojos {self.color_ojos} se fue a dormir...")

    def __init__(self, raza, nombre, color_pelo, color_ojos):
        self.raza = raza
        self.nombre = nombre
        self.color_pelo = color_pelo
        self.color_ojos = color_ojos



dalmata = Perro("Dalmata", "dalti", "blanco", "negros")

chihuahua = Perro("Chihuahua", "stinky", "cafe" , "cafe")


dalmata.ladrar()
chihuahua.ladrar()
chihuahua.dormir()
