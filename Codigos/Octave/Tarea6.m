pkg load database
conn = pq_connect(setdbopts('dbname','tareas','host','localhost','port','5432','user','postgres','password','admin'));

while true
    disp('1. Mostrar todas las canciones');
    disp('2. Buscar por artista');
    disp('3. Buscar por canción');
    disp('4. Salir');
    opcion = input('Elige una opcion: ', 's');

    switch opcion
        case '1'
            N=pq_exec_params (conn, 'select * from tare6;');%ver datos en la tabla
            disp(N.data);
        case '2'
            artista = input('Introduce el nombre del artista: ', 's');
            consulta = sprintf("SELECT * FROM tare6 WHERE artista ILIKE '%%%s%%';", artista);%consulta en la tabla
            rs = pq_exec_params(conn, consulta);
            if isempty(rs.data) %% ve si disp(rs.data)  esta vacio para poner un mensaje que no se encuentra lo que busca
                disp('No se encontraron resultados. Selecciona la opcion 1 para ver los artistas disponibles.');
            else
                disp(rs.data);
            end
        case '3'
            cancion = input('Introduce el nombre de la cancion: ', 's');
            consulta = sprintf("SELECT * FROM tare6 WHERE cancion ILIKE '%%%s%%';", cancion);
            
            rs = pq_exec_params(conn, consulta);
            if isempty(rs.data)
                disp('No se encontraron resultados. Selecciona la opcion 2 para ver las canciones disponibles.');
            else
                disp(rs.data);
            end
        case '4'
            break;
        otherwise
            disp('Opcion no valida');
    end
end