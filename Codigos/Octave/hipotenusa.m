#entre llaves los valores que queremos llamar

#lo que esta en parentesis son los valores que vamos a devolver

function [hipo, a_cuadrada] = hipotenusa (a,b)
    hipo = sqrt(a.^2+ b^2);
    a_cuadrada = a.^2;
endfunction