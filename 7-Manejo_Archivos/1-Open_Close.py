"""
open() y close() permiten manejar archivos con Python
"""

# open
archivo = open('../../test.txt', 'w');

# modos de lectura:
"""
r: Lectura (da error si el archivo no existe)
w: Escritura (borra el contenido si el archivo existe)
a: Agregar contenido al final del archivo
x: Crea un archivo nuevo (error si ya existe)
b: modo binario
t: modo texto, es el default
"""

# Escritura en un archivo
archivo.write('Hola mundo');
archivo.close();

# lectura
archivo = open('../../test.txt', 'r');
contenido = archivo.read();
print(contenido)

"""
Otros metodos:
readline: lee solo una linea
readlines: devuelve una lista con todas las lineas
"""

# Usando with open()
with open('../../test.txt', 'r') as archivo:
    contenido = archivo.read()
    print(contenido)
# No es necesario llamar a close()