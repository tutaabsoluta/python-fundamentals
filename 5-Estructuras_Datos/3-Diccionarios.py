"""
1. Mutables
2. Estructura clave-valor
3. Claves unicas e inmutables
4. Valores de cualquier tipo
5. Mas rapidos que listas para busquedas
6. Compatibles con bucles

Muy usados en JSON, APIs y almacenamiento estructurado de datos

Metodos: get, keys, values, items, pop, update
"""

mi_diccionario = dict( color="rojo" );
print(type(mi_diccionario))

persona = {
    "nombre": "Sergio",
    "edad": 30,
    "profesion":"desarrollador",
};

# Obtener elementos get
print(persona["nombre"]) # Sergio
print(persona.get("edad")) # 30

# Modificar valores
persona["edad"] = 28;
print(persona["edad"]) # 28

# Eliminar elementos pop, popitem
# del persona["edad"]; # Elimina la clave 'edad'
# edad = persona.pop("edad") # Elimina y devuelve el valor de 'edad'
# ultimo = persona.popitem(); # Elimina el último elemento añadido

# Recorrer las claves
persona2 = {
    "nombre": "Sergio",
    "edad": 30,
    "profesion":"desarrollador",
};
for clave in persona2:
    print(clave) # nombre, edad, profesion

# Recorrer los valores

for valor in persona2.values():
    print(valor) # Sergio, 30, desarrollador

# Recorrer clave y valor
for clave, valor in persona2.items():
    print(f"{clave}: {valor}")
