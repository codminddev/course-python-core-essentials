from random import sample
from operaciones import insertar_dato, buscar_palabra, obtener_aleatorios, eliminar_palabra_base

# from database import diccionario

diccionario = []
def agregar_palabras():
    palabra = input("¿Cuál es la palabra que quieres registrar (español) ? ")
    traduccion = input("¿Cuál es la traducción (inglés) ? ")
    try:
        insertar_dato(palabra, traduccion)
        print("Se registró con éxito")
    except Exception as e:
        print("Ocurrió la siguiente excepción")

def recordar_significado(palabra):
    print("Voy a buscar la palabra ", palabra)
    resultado = buscar_palabra(palabra)

    if resultado != None:
        return resultado
    else:
        return "La palabra " + palabra + " no esta registrada en la base"
    
def iniciar_quiz():
    #seleccionadas = sample(diccionario,5)
    seleccionadas = obtener_aleatorios()
    puntacion = 0

    for palabra in seleccionadas:
        respuesta = input(f"¿Qué significa '{palabra['traduccion']}'? ")
        if respuesta == palabra["palabra"]:
            puntacion = puntacion + 2
    
    print(f"Tu puntuación es de {puntacion}")

def eliminar_palabra(palabra):
    eliminar_palabra_base(palabra)

# agregar_palabras()