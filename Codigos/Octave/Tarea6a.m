pkg load database
conn = pq_connect(setdbopts('dbname','tareas','host','localhost','port','5432','user','postgres','password','admin'));

%N=pq_exec_params (conn, 'select * from estudiantes;');%ver datos en la tabla
%disp(N.data);

while true
    disp('1. Agregar nuevo estudiante');
    disp('2. Editar información de estudiante existente');
    disp('3. Eliminar estudiante de la base de datos');
    disp('4. Ver lista de estudiantes')
    disp('5. Salir');
    opcion = input('Elige una opción: ', 's');

    switch opcion
        case '1'
            nombre = input('Introdusca el nombre del estudiante: ', 's');
            edad = input('Introdusca la edad del estudiante: ', 's');
            genero = input('Introdusca el género del estudiante: ', 's');
            direccion = input('Introdusca la dirección del estudiante: ', 's');
            registro = sprintf("INSERT INTO estudiantes (nombre, edad, genero, direccion) VALUES ('%s', %s, '%s', '%s');", nombre, edad, genero, direccion);
            [err, msg] = lasterr();
            try
                N=pq_exec_params(conn, registro);
                disp('Estudiante agregado exitosamente.');
            catch ME
                disp(['Error: ' ME.message]);
            end
        case '2'
            id = input('Introdusca el id del estudiante a editar: ', 's');
            nombre = input('Introdusca el nuevo nombre del estudiante: ', 's');
            edad = input('Introdusca la nueva edad del estudiante: ', 's');
            genero = input('Introdusca el nuevo género del estudiante: ', 's');
            direccion = input('Introdusca la nueva dirección del estudiante: ', 's');
            consulta = sprintf("UPDATE estudiantes SET nombre = '%s', edad = '%s', genero = '%s', direccion = '%s' WHERE id = %s;", nombre, edad, genero, direccion, id);
            [err, msg] = lasterr();
            try
                N=pq_exec_params(conn, consulta);
                disp('Información del estudiante actualizada exitosamente.');
            catch ME
                disp(['Error: ' msg]);
            end
        case '3'
            id = input('Introdusca el ID del estudiante a eliminar: ', 's');
            consulta = sprintf("DELETE FROM estudiantes WHERE id = %s;", id);
            [err, msg] = lasterr();
            try
                pq_exec_params(conn, consulta);
                disp('Estudiante eliminado exitosamente.');
            catch ME
                disp(['Error: ' msg]);
            end
        case '4'
            N=pq_exec_params (conn, 'select * from estudiantes;');
            disp(N.data);
        case '5'
            break;
        otherwise
            disp('Opción no válida');
    end
end
