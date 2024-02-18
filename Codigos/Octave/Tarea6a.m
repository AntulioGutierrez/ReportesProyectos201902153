pkg load database
conn = pq_connect(setdbopts('dbname','tareas','host','localhost','port','5432','user','postgres','password','admin'));

N=pq_exec_params (conn, 'select * from tarea6Siii1;');%ver datos en la tabla
disp(N.data);