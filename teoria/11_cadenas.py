print("Iniciando con procesamiento de cadenas")

mi_cadena = "Este es un texto muy largo"

print(mi_cadena[8:17])

print(mi_cadena[-20:-7])

palabra =  mi_cadena[-5:]

print(palabra.capitalize())
print(palabra.upper())
print(palabra.lower())
print(palabra.swapcase())

index = mi_cadena.find("muy")
print( mi_cadena[index:])

print(mi_cadena.replace("largo", "corto"))

mi_strip = "     texto "
print(mi_strip.strip())
