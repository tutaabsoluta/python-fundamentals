"""
1. No permiten duplicados
2. No estan ordenados
3. Mutables
4. No se pueden anadir diccionarios ni listas
5. No soporta indexacion ni slicing

Útiles para eliminar duplicados y optimizar búsquedas.
Perfectos para manejar datos únicos de forma eficiente!

Funciones: add, remove, discard, clear
"""

mi_set = {1,2,3,4,5,6};

# Creando un set con set()
otro_set = set([1,2,3,4,5]);

# No permite valores duplicados
numeros = {1, 2, 2, 3, 4, 4, 5}
print(numeros)
# {1, 2, 3, 4, 5}  # No hay duplicados

# agregar elementos
mi_set = {1, 2, 3}
mi_set.add(4)  # Agrega 4
print(mi_set)
# {1, 2, 3, 4}

# Eliminar remove, discard
mi_set.remove(2)  # Elimina el 2, da error si no existe
mi_set.discard(5)  # No da error si 5 no está en el set
print(mi_set)

# Eliminar un elemento aleatorio
valor = mi_set.pop()  # Elimina y devuelve un elemento aleatorio
print(valor)
print(mi_set)

# Vaciar el set
mi_set.clear()  # Deja el set vacío
print(mi_set)  # set()

# Operacion de conjuntos: los sets soportan operaciones matemáticas como unión, intersección y diferencia.
# Union
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)
# {1, 2, 3, 4, 5}

# Interseccion
print(a & b)
# {3}  # Elementos en común

# Diferencia
print(a - b)
# {1, 2}  # Elementos en `a` que no están en `b`

# Convertir entre listas y sets para eliminar duplicados
lista = [1, 2, 2, 3, 4, 4, 5]
sin_duplicados = list(set(lista))
print(sin_duplicados)
# [1, 2, 3, 4, 5]