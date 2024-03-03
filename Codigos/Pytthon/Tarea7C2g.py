#inicilaizacion de variables
contardor = 0

# Bucle while que se ejecuta mientras contador sea menor a 5
while contardor < 5:
    print(contardor)
    contardor +=1
print('fuera del bucle')

# pide al ususairo que introduzca un numero positivo
numero = int(input("introduce un nuemro positivo: "))

#mientras el numero no sea positivo, sigue pidiendo al usuario que introduzca un numero
while numero <= 0:
    print("eos no es un numero positivo. intente de nuevo")
    
print(f"has introducido un numero positivo: {numero}")