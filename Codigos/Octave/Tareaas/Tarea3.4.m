n=-3:7;
x=0.55.^(n+3);
h=[1 1 1 1 1 1 1 1 1 1 1];
y=conv(x, h);
subplot(311);
stem(x);
title('Señal Original');
subplot(312);
stem(h)%Usa stema para secuencias discretas
title('Respuesta al Impulsa / Segunda Señal ');
subplot(313);
stem(y);
title('Convolucion Resultante');