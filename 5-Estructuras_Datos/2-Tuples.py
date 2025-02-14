"""
1. Inmutables
2. Ordenadas
3. Puede contener distintos tipos de datos
4. Se pueden repetir elementos
5. Mas rapidas que las listas

Metodos: count, index
"""

mi_tupla = (1,2,3,True);

otra_tuplas = 1,2,3; # reconocida por Python como tupla

lenguajes = ('JavaScript', 'Python', 'C#');

# Slicing de tuples
print(lenguajes[:2]) # JavaScript, Python
print(lenguajes[1:]) # Python, C#
print(lenguajes[:1]) # JavaScript

# Desempaquetar tuple
frutas = ('Manzana', 'Pera', 'Melocoton');
manzana, pera, melocoton = frutas;

print(manzana)

# Metodos de tuples

# Count
print(frutas.count('Manzana')) # 1

# Index
print(frutas.index('Pera')) # 1
