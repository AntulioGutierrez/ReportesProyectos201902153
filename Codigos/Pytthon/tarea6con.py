import psycopg2

# Establecer la conexión a la base de datos
conn = psycopg2.connect(
    dbname="tareas",
    user="postgres",
    password="admin",
    host="localhost"
)

while True:
    print("1. jugar")
    print("2. instrucciones")
    print("3. ver preguntas")
    print("4. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        res = input("Introduce la respuesta correcta: ")
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM concurso WHERE respuesta = %s;", (res))
            rows = cur.fetchall()
            for row in rows:
                print(row)
    elif opcion == "2":
        artista = input("Introduce el nombre del artista: ")
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM canciones WHERE artista = %s;", (artista,))
            rows = cur.fetchall()
            for row in rows:
                print(row)
    elif opcion == "3":
        
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM canciones;")
            rows = cur.fetchall()
            for row in rows:
                print(row)
    elif opcion == "4":
        break
    else:
        print("Opción no válida")

        