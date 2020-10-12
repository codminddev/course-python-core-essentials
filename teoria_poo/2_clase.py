class Palabra:
    palabra = None
    traduccion = None
    __porcentaje = 0

    def __init__(self, palabra, traduccion):
        self.palabra = palabra
        self.traduccion = traduccion
    
    def cambia_porcentaje(self):
        self.__porcentaje += 25

    def mostrar_porcentaje_avance(self):
        print(f"Tu porcentaje de avance es {self.__porcentaje} %")
    
    def preguntar_palabra(self):
        resultado = input(f"¿Qué significa la palabra '{self.traduccion}'? ")
        if resultado == self.palabra:
            self.cambia_porcentaje()
    

mi_palabra = Palabra("perro","dog")
mi_palabra_2 = Palabra("gato","cat")


print(mi_palabra.__dict__)

mi_palabra_2.preguntar_palabra()

mi_palabra_2.preguntar_palabra()

mi_palabra_2.mostrar_porcentaje_avance()
