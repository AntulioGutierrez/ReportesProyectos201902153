def procesar_datos(numero, cadena, lista):
    """esta funcion toma un entero, una cadena, y una lista, y realiza opereaciones en cada uno."""
    
    # dobla el numero 
    numero = numero *2
    
    # convierte la cadena en mayuscualas 
    cadena = cadena.upper()
    
    # añade un elemento a la lista 
    lista.append("nuevo elemento")
    
    # devuelve los nuevos valores
    return numero, cadena, lista

mi_numero = 5
mi_cadena = "Hola mundo"
mi_lista = ["elemento 1", "elemento 2"]

nuevo_numero, nueva_cadena, nueva_lista = procesar_datos(mi_numero, mi_cadena, mi_lista)

print(f"el nuevo numero es {nuevo_numero}")
print(f"el nueva cadeba es {nueva_cadena}")
print(f"el nueva lista es {nueva_lista}")