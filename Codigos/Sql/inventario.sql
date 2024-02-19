CREATE TABLE inventario (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    descripcion TEXT,
    cantidad INTEGER,
    precio DECIMAL(10, 2)
);

select * from inventario;