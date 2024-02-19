pkg load database
conn = pq_connect(setdbopts('dbname','tareas','host','localhost','port','5432','user','postgres','password','admin'));

while true
    disp('1. Agregar producto');
    disp('2. Actualizar producto');
    disp('3. Eliminar producto');
    disp('4. Mostrar todos los productos')
    disp('5. Salir');
    opcion = input('Elige una opción: ', 's');

    switch opcion
        case '1'
            nombre = input('Introdusca el nuevo producto: ', 's');
            descripcion = input('Introdusca descripcion del producto: ', 's');
            cantidad = input('Introdusca la cantidad del producto: ', 's');
            precio = input('Introdusca el precio del producto: ', 's');
            registro = sprintf("INSERT INTO inventario (nombre, descripcion, cantidad, precio) VALUES ('%s', '%s', '%s', %s);", nombre, descripcion, cantidad, precio);
            [err, msg] = lasterr();
            try
                N=pq_exec_params(conn, registro);
                disp('Producto agregado exitosamente.');
            catch ME
                disp(['Error: ' ME.message]);
            end
        case '2'
            id = input('Introdusca el id del producto a editar: ', 's');
            nombre = input('Introdusca el nuevo nombre producto: ', 's');
            descripcion = input('Introdusca la nueva descripcion del producto: ', 's');
            cantidad = input('Introdusca nueva la cantidad del producto: ', 's');
            precio = input('Introdusca el nuevo precio del producto: ', 's');
            actualizar = sprintf("UPDATE inventario SET nombre = '%s', descripcion = '%s', cantidad = '%s', precio = '%s' WHERE id = %s;", nombre, descripcion, cantidad, precio, id);
            [err, msg] = lasterr();
            try
                N=pq_exec_params(conn, consulta);
                disp('Información del producto actualizada exitosamente.');
            catch ME
                disp(['Error: ' msg]);
            end
        case '3'
            id = input('Introdusca el ID del producto a eliminar: ', 's');
            eliminar = sprintf("DELETE FROM inventario WHERE id = %s;", id);
            [err, msg] = lasterr();
            try
                pq_exec_params(conn, consulta);
                disp('Producto eliminado exitosamente.');
            catch ME
                disp(['Error: ' msg]);
            end
        case '4'
            N=pq_exec_params (conn, 'select * from inventario;');
            disp(N.data);
        case '5'
            disp('Saliendo del programa...');
            break;
        otherwise
            disp('Opcion no valida. Elija otra.');
    end
end
