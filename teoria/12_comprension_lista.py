# 1) Tranformar una lista , map
# 2) Filtrar una lista, filter

lista = []

for i in range(10):
    lista.append(i)

print(lista)

# [expresion for elemento in iterable]

lista_cuadrada = [i*i for i in range(10)]

print(lista_cuadrada)

lista_cuadrada_filtro = [i*i for i in range(10) if i % 2 == 0]

print(lista_cuadrada_filtro)

lista_cuad_filt_2 = [i*i if i % 2 == 0 else 0 for i in range(10) ]

print(lista_cuad_filt_2)