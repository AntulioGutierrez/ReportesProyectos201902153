#Estructuras de control de frujo
x=1
y =0
z = -5 
if (x>y)
    'X es mayor a y'
elseif (x==y)
    'X y Y son iguales'
else
    'Y es  mayor a X'
endif

if (x>y & z<0)
    'X es mayor a Y y Z es menor a 0'
elseif (x==y | z<0)
    'X y Y son iguales o Z es menor a 0'
else
    'Y es  mayor a X'
endif

while (z<y)
    z
    ++z
endwhile

fib = ones(1,10);
for i  =3:10
    fib(i) = fib(i-1) + fib(i-2);
endfor
fib

try
    m = [1:5; 10:15]#no es correcto poq hay un valor mas en la matriz
catch
    'No se puede ejecutar el codigo, luego se continua con el codigo'
end_try_catch

#Operacion con Matrices
M = [1,2,7; 4,5,11; 0.1,0.2,0.3]
N = [0,1,2 ;8,10,12;0x177, 0x176, 0x125]
M + N
M-N
M*N
cross(M,N) #M *N
dot ( M,N)
M'
