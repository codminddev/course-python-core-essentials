from funcionalidades import agregar_palabras, recordar_significado, iniciar_quiz, eliminar_palabra
import time

continuar = True
while continuar:
    print("1) Agregar palabras")
    print("2) Consultar significado")
    print("3) Jugar")
    print("4) Eliminar palabra")
    print("0) Salir" )

    opcion = input("¿Qué quieres hacer? ")

    if opcion == "1":
        agregar_palabras()
    elif opcion == "2":
        print("Consultando significado...")
        palabra = input("Escribe la palabra en español para traducir? ")
        significado = recordar_significado(palabra)
        print("Resultado: " + significado )
    elif opcion == "3":
        print("Ok vamos  a jugar")
        iniciar_quiz()
    elif opcion == "0":
        print("Hasta luego gracias por aprender idiomas")
        continuar = False
    elif opcion == "4":
        print("Eliminando palabra...")
        palabra = input("¿Cuál es la palabra que deseas eliminar?")
        try:
            eliminar_palabra(palabra)
            print("se eliminó la palabra")
        except Exception as e: 
            print("ocurrió un error", e)
    else:
        print("Opción no válida")
    print("  --------   ")
    time.sleep(2)

