"""
El scope o ámbito de una variable define dónde puede ser accedida dentro del código.
En Python, el scope se divide en diferentes niveles, que determinan la visibilidad de variables dentro y fuera de las funciones.

Tipos de Scope
Local (L) – Variables dentro de una función.
Enclosing (E) – Variables en funciones anidadas.
Global (G) – Variables declaradas fuera de funciones.
Built-in (B) – Variables y funciones predefinidas en Python.
"""

# Scope local: las variables edclaradas dentro de una funcion solo son accesibles dentro de esa funcion

def funcion():
    x = 10
    print(x)

# Scope global: las variables globales son accesibles desde cualquier parte del codigo
x = 10

def mostrar():
    print(x)
mostrar()  # Salida: 10
print(x)   # Salida: 10

# Modificar variables globales
def modificar():
    global x
    x = 15
    return x

print(modificar())

# Scope enclosing: funciones anidadas, cuando una funcion esta dentro de otra, la funcion interna puede acceder a valores de la funcion externa

def externa ():
    mensaje = 'Hola'

    def interna():
        print(mensaje)

# Modificar variables de funcion externa
def externa():
    mensaje = "Hola"

    def interna():
        nonlocal mensaje  # Modifica la variable de la función externa
        mensaje = "Hola desde interna"

    interna()
    print(mensaje)  # Salida: Hola desde interna

# Scope Built-in: son las funciones y palabras clave predefinidas en Python
print(len("Python"))  # len() es una función built-in