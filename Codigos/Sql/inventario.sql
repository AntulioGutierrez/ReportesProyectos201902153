--CREATE TABLE inventario (id SERIAL PRIMARY KEY, nombre VARCHAR(100), descripcion TEXT, cantidad INTEGER, precio DECIMAL(10, 2));

--ALTER TABLE inventario DROP COLUMN precio;
--ALTER TABLE inventario ADD COLUMN precio float;
select * from inventario;