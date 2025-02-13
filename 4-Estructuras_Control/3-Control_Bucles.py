
# break: salir de un bucle

for i in range(10):
    if i == 5:
        break # detiene el ciclo cuando llega a 5
    print(i)

# continue: salta a la siguiente iteracion
for i in range(5):
    if i == 2:
        continue # se salta el 2 y continua iterando
    print(i)

# pass: no hace nada, sirve como placeholder

for i in range(5):
    if i == 2:
        pass
    print(i)