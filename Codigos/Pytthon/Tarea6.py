import psycopg2

# Establecer la conexión a la base de datos
conn = psycopg2.connect(
    dbname="test",
    user="usuario",
    password="admin",
    host="localhost"
)

while True:
    print("1. Mostrar todas las canciones")
    print("2. Buscar por artista")
    print("3. Buscar por canción")
    print("4. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM canciones;")
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
        cancion = input("Introduce el nombre de la canción: ")
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM canciones WHERE cancion = %s;", (cancion,))
            rows = cur.fetchall()
            for row in rows:
                print(row)
    elif opcion == "4":
        break
    else:
        print("Opción no válida")
