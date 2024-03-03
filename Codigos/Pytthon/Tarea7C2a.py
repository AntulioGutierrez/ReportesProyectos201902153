print('1.Indexacion de los strings: ')
s = "Hola Mundo"
print(s[0]) # imprime "H"
print(s[4]) # imprime " "
print(s[-1]) #imprime "o"

print('2. cortar un string (Slicing): ')
s = "Hola Mundo"
print(s[0:4]) #imprime "hola"
print(s[5:]) # imprime "mundo"

print('concatenar strings: ')
s1= "Hola"
s2= "mundo"
s3 = s1+ " "+ s2 # concatena los strings con un espacio en medio 
print(s3) #imprime " Hola mundo"

print('4. Cambiar un valor en un string: ')
s="Hola mundo"
s = s.replace("m", "M") # Reemplaza "m" con "M"
print(s) #imprime "Hola Mundo"

print("5. Metodos de los strings: ")
s= " Hola Mundo "

print(s.upper()) #pone todo con mayusculas
print(s.lower()) # pone todo con minusculas
print(s.replace("H", "h")) # remplaza letras con otras
print(s.lstrip()) #Elimina los espacios antes del mensaje
print(s.rstrip()) #Elimina los espacios despues del mensaje
print(s.strip()) # elimimna los espacios antes y despues del mensaje
print(s.split()) #nos devuelve una lista de nuestro mensaje siendo cada palabra un objeto de nuestra lista