print('1. Ejemplo de diccionnario: ')
# definicion de un diccionario
mi_diccionario = {"Clave 1 ": "Valor 1","Clave 2 ": "Valor2","Clave 3": "Valor 3",}
print(mi_diccionario)

print('2. Acceder a un valor de una clave: ')
print(mi_diccionario["Clave 1 "]) # muestra el "valor 1"

print('3. Asignar un nuevo valor a una clave: ')
mi_diccionario["Clave 1 "] = "nuevo valor 1"
print(mi_diccionario)

print('4. iteracion de un diccionario: ')
for clave, valor in mi_diccionario.items():
    print(f"la clave es '{clave}' y el valor es '{valor}'")
 
print('5. metodos de los diccionarios: ')   
# copia el diccionario 
nuevo_diccionario = mi_diccionario.copy()
print(nuevo_diccionario)

#crea un nuevo diccionario con la calves dada  y el mismo valor 
claves = ('clave 1', 'clave2', 'clave3')
valor = 'valor'
diccionario_fromkeys = dict.fromkeys(claves, valor)
print(diccionario_fromkeys)

# devuelve el valor para la clave especificada si existe
print(mi_diccionario.get("clave 1"))

# Comprueba si la clave especificada existe en el diccionario
print("Clave 1" in mi_diccionario)

# mostrar tods los valores en una lista clave- valor
print(mi_diccionario.items())

# mostrar en una lista todas las claves
print(mi_diccionario.keys())

# actualizar el diccionario con los pares clave-valor  especificados
mi_diccionario.update({"Clave 1 ": "nuevo Valor 1","Clave 2 ": "nuevo Valor2","Clave 4": "Valor 4"})

# muestra una lista de toos los valores
print(mi_diccionario.values())

# limpia todo el diccionario 
mi_diccionario.clear()
print(mi_diccionario)

