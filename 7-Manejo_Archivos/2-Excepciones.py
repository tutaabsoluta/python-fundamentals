"""
Excepciones en el manejo de archivos
Para evitar errores al trabajar con archivos, se usan excepciones.
"""

try:
    archivo = open('../../test.txt', 'r')
    contenido = archivo.read()
except FileNotFoundError:
    print('El archivo no existe')
finally:
    print('Fin del programa')