import psycopg2
import random

def obtener_preguntas():
    conn = psycopg2.connect(database="tareas", user="postgres", password="admin", host="localhost", port="5432")
    cur = conn.cursor()
    cur.execute("SELECT pregunta, respuesta FROM tu_tabla")
    preguntas = cur.fetchall()
    conn.close()
    return preguntas

def jugar():
    preguntas = obtener_preguntas()
    random.shuffle(preguntas)
    vidas = 3
    puntos = 0
    for i in range(5):
        print(f"Pregunta {i+1}: {preguntas[i][0]}")
        respuesta = input("Tu respuesta: ")
        if respuesta.lower() == preguntas[i][1].lower():
            puntos += 1
            print("¡Correcto!")
        else:
            vidas -= 1
            print("Incorrecto.")
        print(f"Puntos: {puntos}, Vidas: {vidas}")
        if vidas == 0:
            break
    print(f"Puntuación final: {puntos}")

def instrucciones():
    print("Instrucciones del juego:")
    print("1. Tendrás inicialmente 3 vidas.")
    print("2. Deberás ingresar tu respuesta para cada pregunta.")
    print("3. En caso de acertar, se sumará un punto.")
    print("4. En caso de fallar, se quitará una vida.")
    print("5. Tras haber realizado 5 preguntas, se presentará la puntuación final.")

def menu():
    while True:
        print("1. Jugar\n2. Instrucciones del juego\n3. Mostrar pregunta\n4. Salir")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            jugar()
        elif opcion == "2":
            instrucciones()
        elif opcion == "3":
            preguntas = obtener_preguntas()
            for pregunta in preguntas:
                print(pregunta[0])
        elif opcion == "4":
            break

menu()
