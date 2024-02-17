%Generar señal senoidal
fs = 1000; % frecuencia de muestreo
t = 0: 1/fs :1; % Vector de tiempo
f = 100; %frecuencia de la señal
x = sin(2*pi*f*t); % señal senoidal

%Aplicar Transformada de fourier
xf = fft(x);

% Generar filtro pasa-bajo
n = length(x);
fcutoff = 50; % Frecuencia de corte
h = ones(n,1); % vector de ceros
h(round(n*fcutoff/fs)+1:end) = 0; %aplicar el filtro pasa-bajo

% Aplicar fitro a la señal en el Dominio de la Frecuencia
xf_filtered = xf .* h;

% Convertir señalFiltrada a dominio del tiempo
x_filtered = ifft(xf_filtered);

%Graficar señal original y señal filtradad
figure;
subplot(2,1,1);
plot(t, x);
title('Señal original');
xlabel('Tiempo (s)');
ylabel('Amplitud ');
subplot(2,1,2);
plot(t, real(x_filtered));
title('Señal filtradad');
xlabel('Tiempo (s)');
ylabel('Amplitud ');