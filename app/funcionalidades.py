from random import sample

from database import diccionario

def agregar_palabras():
    palabra = input("¿Cuál es la palabra que quieres registrar (español) ? ")
    traduccion = input("¿Cuál es la traducción (inglés) ? ")
    nueva_palabra = {"palabra": palabra , "traduccion": traduccion}
    diccionario.append(nueva_palabra)
    # print("Ahora tienes " + str(len(diccionario)) + " palabras")
    print(f"Ahora tienes {len(diccionario)} palabras")

def recordar_significado(palabra):
    print("Voy a buscar la palabra ", palabra)
    # for elemento in diccionario:
    #     if elemento["palabra"] == palabra:
    #         print(elemento)
    #         return elemento["traduccion"]
    
    resultado = [elemento["traduccion"] for elemento in diccionario if elemento["palabra"] == palabra ]
    if len(resultado) == 1:
        return resultado[0]
    else:
        return "La palabra " + palabra + " no esta registrada en la base"
    
def iniciar_quiz():
    seleccionadas = sample(diccionario,5)
    puntacion = 0

    for palabra in seleccionadas:
        respuesta = input(f"¿Qué significa '{palabra['traduccion']}'? ")
        if respuesta == palabra["palabra"]:
            puntacion = puntacion + 2
    
    print(f"Tu puntuación es de {puntacion}")

# agregar_palabras()