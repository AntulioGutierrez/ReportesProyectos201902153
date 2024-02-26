pkg load database %cargar el paquete
conn = pq_connect(setdbopts('dbname','tareas','host','localhost','port','5432','user','postgres','password','admin'))

%%N=pq_exec_params (conn, "delete from redes where nombre= 'Antulio';") % borrar registros de datos en la tabla
%%N=pq_exec_params (conn, "insert into redes values ('Antulio', 201902153);") % insertar datos en la tabla
N=pq_exec_params (conn, 'select * from tare6;')%ver datos en la tabla
