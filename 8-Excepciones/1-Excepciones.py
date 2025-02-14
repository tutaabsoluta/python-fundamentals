"""
Las excepciones en Python ocurren cuando un error interrumpe la ejecución del programa.
En lugar de que el código falle completamente, Python permite manejar estos errores con try, except, else, finally.
"""

try:
    resultado = 10 / 0
except ZeroDivisionError:
    print('No se puede dividir entre 0')

# Ejemplo con multiples excepciones

try:
    numero = int(input('Ingresa un numero: '))
    resultado = 10 / numero
except ZeroDivisionError:
    print('No puedes dividir por cero')
except:
    print('Debes ingresar un numero valido')
else:
    print(resultado)

# Lanzamiento de excepciones con raise()
# raise permite forzar un error

numero = int(input('Ingresa un numero'))

if numero < 0:
    raise ValueError('No se permiten valores negativos')