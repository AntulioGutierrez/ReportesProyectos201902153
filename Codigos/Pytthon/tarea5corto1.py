# crear variables e importar la funcion os para borrar archivo
import os
archivo = 'imc.txt'
opc = -1

# menu principal del programa
while opc != 0:
    #opciones del usuario
    print('1. Calcular IMC')
    print('2. Guardar IMC en archivo')
    print('3. Leer IMC de archivo')
    print('4. Borrar archivo de IMC')
    print('0. Salir')
    opc = int(input('Elige una opción: '))

    if opc == 1:
        # Calcular IMC
        nombre = str(input('Nombre del usuario: '))
        peso = float(input('Introduce tu peso en kg: '))
        altura = float(input('Introduce tu altura en m: '))
        imc = peso / altura**2
        print('Tu IMC es '+ '\n')
        print(imc)
        if imc < 18.5:
            print('Bajo peso')
        elif imc < 24.9:
            print('Normal')
        elif imc < 29.9:
            print('Sobrepeso')
        else:
            print('Obesidad')
    elif opc == 2:
        # Guardar IMC en archivo
        with open(archivo, 'a') as f:
            f.write('El nombre del usuraio es: ' + nombre + '\n')
            f.write('El peso del usuraio es: '+ str(peso) + '\n')
            f.write('La altura del usuraio es: '+ str(altura) +'\n')
            f.write('El IMC del usuraio es:'+ str(imc) + '\n' )
    elif opc == 3:
        # Leer IMC de archivo
        try:
            with open(archivo, 'r') as f:
                imc_guardado = f.read()
            print('IMC guardado: ')
            print(imc_guardado)
        except FileNotFoundError:
            print('No hay datos de IMC guardados.')
    elif opc == 4:
        # Borrar archivo de IMC
        try:
            os.remove(archivo)
            print('Archivo de IMC borrado.')
        except FileNotFoundError:
            print('No hay archivo de IMC para borrar.')
    elif opc == 0:
        # Salir
        print('¡Gracais por usar el programa!')
    else:
        print('Opcion no valida por favor, elige una opcion del menu')