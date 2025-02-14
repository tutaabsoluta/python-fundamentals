# Funcion: bloque de codigo reutilizable que hace una tarea especifica

def saludar ():
    print('Hola Sergio')

saludar();

# Funciones con parametros y retorno de valores
def sumar( a, b ):
    return a + b

print(sumar(1,2))

numero = sumar(1, 10);
print(numero)

# Funciones con argumentos por default
def multiplicar( a, b = 2 ):
    return a * b

print(multiplicar(2))

# Funciones con *args, numero variable de argumentos
def suma_total(*numeros):
    return sum(numeros)

print(suma_total(1,2,3,4,5,6))

# Funciones con kwargs
"""
**kwargs permite que la función acepte cualquier número de argumentos de palabra clave.
Dentro de la función, kwargs es un diccionario que contiene los pares clave-valor de los argumentos pasados.

Uso comun:
Util cuando quieres que tu función sea flexible y pueda aceptar un número variable de argumentos de palabra clave 
sin necesidad de definirlos todos en la firma de la función.

Herencia: Cuando extiendes una clase y quieres pasar argumentos adicionales a la clase base.

Decoradores: Cuando defines decoradores que pueden ser aplicados a funciones con diferentes firmas.

APIs: Cuando construyes APIs que necesitan ser extensibles y aceptar opciones adicionales.
"""

persona = {
    "nombre": "Sergio",
    "edad": 30,
    "profesion": "desarrollador"
};

def funcion_kwargs (**kwargs):
    for clave, valor in persona.items():
        print(clave, valor)

funcion_kwargs()

#  Funciones lambda (anonimas): funciones de una sola línea, ideales para operaciones simples.

cuadrado = lambda x: x ** 2
print(cuadrado(2))

suma = lambda x: x + 2
print(suma(3))

# Funciones recursivas: se llaman a si mismas
def factorial(n):
    if n == 0:
        return  n * factorial(n - 1)