
# and: evalúa a True si ambas condiciones son verdaderas.
numero1 = 5;
numero2 = 6;
numero3 = 3;

if ( numero1 < numero2 and numero1 > numero3 ):
    print(f'{numero1} es menor a {numero2} y mayor a {numero3}')

# or: evalúa a True si al menos una de las condiciones es verdadera.
a = 5;
b = 10;

print( a > b or b > 20 ); # true, la primer condicion es true

# not: Invierte el valor de la condición: si es True, lo convierte en False, y viceversa.
a = 5;

print(not a > 0); # falso, porque 5 es mayor a cero pero lo invierte
print( not a < 0 ); # verdadero, porque 5 no es menor a 0 pero lo invierte