#OBJETOS NUMERICOS
375
3.75e2
3.75E2
0x177

#numero_inicial:salto:numero_final
1:10
1:0.5:10
#tener en cuenta que tiene que estar dentro del rango la suma final de los saltos

#matrices
M = [1,2,3; 4,5,6; 7,8,9]
N = [1:4; 5:8]

#cadena String '' o ""
'cadena de string'
"cadena de string"
#"\\"
#"\a"

#estructuras
x =()
x.secuencia = 1:5
x.matriz = [1,2; 44, 5]
x
x.estructura={}
x.estructura.numero = 0x177
x.estructura.letra ='A'

#tipos de operadores
x = 2 
y = 3
x+y
x-y
x*y
x/y
++x # x = x +1 
--x # x = x -1 

#devuelven un 1 o 0 
x < y
x <=y
x == y 
x > y
x >= y 
x != y

#flujo 
x = 0 
y = 1
x & y #and
x | y #or
not(x)