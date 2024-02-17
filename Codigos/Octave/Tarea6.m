pkg load database
conn = pq_connect(setdbopts('dbname','tareas','host','localhost','port','5432','user','postgres','password','admin'));

while true
    disp('1. Mostrar todas las canciones');
    disp('2. Buscar por artista');
    disp('3. Buscar por canción');
    disp('4. Salir');
    opcion = input('Elige una opción: ', 's');

    switch opcion
        case '1'
            N=pq_exec_params (conn, 'select * from tare6;');%ver datos en la tabla
            disp(N.data);
        case '2'
            artista = input('Introduce el nombre del artista: ', 's');
            query = sprintf("SELECT * FROM tare6 WHERE artista LIKE '%%%s%%';", artista);
            rs = pq_exec_params(conn, query);
            disp(rs.data);
        case '3'
            cancion = input('Introduce el nombre de la canción: ', 's');
            query = sprintf("SELECT * FROM tare6 WHERE cancion = '%s';", cancion);
            rs = pq_exec_params(conn, query);
            disp(rs.data);
        case '4'
            break;
        otherwise
            disp('Opción no válida');
    end
end