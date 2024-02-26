#funciones

#en la ventana de comandos 
#edit prueba.m
#edit hipotenusa.m

#para llamar una funcion

#lo que esta en parentesis son los valores que entran a nuestra funcion
[x, b] = hipotenusa (2 ,2)


#graficas
x = [-3:0.1:1]; o #x = linspace(-3,1,50);
plot(x, funcion(x), 'Color', 'Green', 'LineStyle', ':');
title('Titulo');
ylabel('eje y');
xlabel('eje x');

#para plotear o hacer un muestreo
x = linspace(-3,1,50);
stem(x, funcion(x), 'Color', 'red', 'LineStyle', ':');
title('Titulo');
ylabel('eje y');
xlabel('eje x');
legend('funcion')

#dos grafiacas en una sola figura
x = [0:0.1:4*pi];
y1 = sin (x);
y2 = cos(x);
hold on;
p1 = plot (x,y1);
p2 = plot (x, y2);
set(p1,'Color', 'red', 'LineWidth', 2);
set(p2,'Color', 'red', 'LineWidth', 1);
title('Titulo');
ylabel('eje y');
xlabel('eje x');
legend('seno', 'coseno')
hold off;