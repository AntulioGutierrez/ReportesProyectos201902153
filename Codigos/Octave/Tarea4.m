%comprueba version
if(exist('OCTAVE_VERSION','builtin')~=0)
    %Estamos en octave
      pkg load signal;
end
%menu principal
opcion = 0;
while opcion ~= 5
%opcion = input('Seleccione una opcion: \n 1. Grabar audio\n 2. Reproducir audio\n 3. Grabar audio\n 4. Salir\n');
%menu de opciones
disp('Seleccione una opcion:')
disp('1. Grabar')
disp('2. Reproducir')
disp('3. Graficar audio')
disp('4. Graficar espectro de frecuencia')
disp('5. Salir')
opcion = input('ingrese su eleccion: ');
switch opcion
    case 1
        %grabar audio
    try
        duracion = input('Ingrese la duracion de la grabacion en segundos: ');
        disp('Comenzando la grabacion...');
        recObj = audiorecorder;
        recordblocking(recObj, duracion);
        disp('Grabacion finalizada.');
        data = getaudiodata(recObj);
        audiowrite('audio.wav',data,recObj.SampleRate);
        disp('Archivo de audio grabado correctamente.');
    catch
        disp('Error al grabar el audio.');
    end
    case 2
        %reproduccion de audio
    try
        [data,fs] = audioread('audio.wav');
        sound(data, fs);
    catch
        disp('Error al reproducir el audio.');
    end
    case 3
        % Grafica de audio
    try
        [data, fs] = audioread('audio.wav');
        tiempo = linspace(0, length(data)/fs, length(data));
        plot(tiempo,data);
        xlabel('Tiempo (s)');
        ylabel('Amplitud');
        title('Audio');
    catch
        disp('Error al graficar el audio');
    end
    case 4
        % Graficando espectro de frecuancia
    try
        disp('Graficando espectro de frecuencia...');
        [audio, Fs] = audioread('audio.wav'); %lee la se?al desde el archivo wav
        N = length(audio); % Numero de muestras de la se?al
        f = linspace(0, Fs/2, N/2+1); % Vector de frecuencia
        ventana = hann(N); %Ventana de Hann para reducir el efecto de las discontinuidades al calcular la FFT
        Sxx = pwelch(audio, ventana, 0, N, Fs); % Densidad espectral de frecuancia
        plot(f, 10*log10(Sxx(1:N/2+1))); %Grafica el espectro de frecuancia en dB
        xlabel('Frecuancia (Hz)');
        ylabel('Densidad espectral de potencia (dB/Hz)');
        title('Espectro de frecuencia de la señal grabada');
    catch
        disp('Error al graficar el audio.');
    end
    case 5
        %salir
        disp('Saliendo del programa...');
    otherwise   
        disp('Opcion no valida.');
    end
end