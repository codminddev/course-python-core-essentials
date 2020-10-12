## Herencia
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

### 
class Sustantivo(Palabra):

    def __init__(self, palabra, traduccion):
        super().__init__(palabra, traduccion)
    
    def preguntar(self):
        self.preguntar_palabra()

class Verbo(Palabra):

    def __init__(self, palabra, traduccion, pasado, participio):
        super().__init__(palabra, traduccion)
        self.pasado = pasado
        self.participio = participio
    
    def preguntar_palabra(self):
        resultado_verbo = input(f"¿Qué significa la palabra '{self.traduccion}'? ")
        resultado_pasado = input(f"¿Cómo se dice el pasado de '{self.palabra}'? ")
        resultado_participio = input(f"¿Cómo se dice el pasado participio de '{self.palabra}'? ")

        if resultado_verbo == self.palabra and resultado_pasado == self.pasado and resultado_participio == self.participio :
            print("Perfecto vas aprendiendo!")
            self.cambia_porcentaje()
        else:
            print("Te equivocaste")
    


sustantivo = Sustantivo("vaso", "glass")
# sustantivo.preguntar()
verbo_1 = Verbo("go", "ir", "went" , "gone")
verbo_2 = Verbo("look", "mirar", "looked", "looked")

verbo_1.preguntar_palabra()




