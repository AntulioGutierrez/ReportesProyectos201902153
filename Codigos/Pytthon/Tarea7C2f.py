print(' 1. ejemplo de tupla')
mi_tupla = (1, "dos", 3.0, True, [5, 0])
print(mi_tupla)

print('2. operaiciones con tuplas: ')
mi_tupla = (1, 2, 5, 3, 2, 4)

# cuenta el numero de veces que aparece un elemento en la tupla
conteo = mi_tupla.count(2)
print(conteo)

# muestra el indice del primer elemento con el valor especificado
indice = mi_tupla.index(3)
print(indice)