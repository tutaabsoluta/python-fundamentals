"""
1. Mutables
2. Ordenadas
3. Heterogeneas
4. Permiten duplicados
5. Indexadas
6. Compatibles con bucles

Metodos:
- Agregar: append, insert
- Eliminar: pop, remove
- Ordenar: sort, sorted
"""

my_list = [1,2,3,4,5];

# Primer elemento

print(my_list[0]);

# Ultimo elemento
print(my_list[-1])

# Modificar un elemento
my_list[0] = 10;
print(my_list[0])

# Anadir elementos al final de la lista
my_list.append(12)
print(my_list)

# Anadir elementos en cualquier posicion
my_list.insert(4, 12);
print(my_list)

# Eliminar elementos (elimina el primer elemento pasado como argumento)
my_list.remove(12)
print(my_list)

# Eliminar elementos en una posicion especifica
eliminado = my_list.pop(2);
print(eliminado)

# Ordenar una lista (modifica la original)
my_list.sort() # ordena de menor a mayor

# Ordenar una lista, creando una nueva
listaOrdenada = sorted(my_list)

# Longitud de una lista
print(len(my_list))