def mi_funcion_saludar( nombre ):
    # print("Aquí inicia mi funcion")
    print("Hola " + nombre)


mi_funcion_saludar("Jorge")
mi_funcion_saludar("Pedro")
mi_funcion_saludar("Juan")

def aplicar_descuento(costo_total, porcentaje_decuento):
    resultado = costo_total / (1 + porcentaje_decuento)
    # print(resultado)
    return resultado


mi_resultado1 = aplicar_descuento(2000, .32)
mi_resultado2 = aplicar_descuento(600, .21)

print("Los resultados son", mi_resultado1, mi_resultado2)