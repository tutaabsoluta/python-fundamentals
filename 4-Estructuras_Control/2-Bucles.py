
# for

numeros = [1,2,3,4,5,6];

for numero in numeros:
    print(numero)

frutas = ['manzana','pera','melocoton'];

for fruta in frutas:
    print(fruta)

# for con range

for i in range(12):
    print(i)

# while: cuando no se conoce de antemano el número de iteraciones y se necesita una condición para detenerlo.

contador = 0;

while contador < 5:
    print(contador)
    contador +=1

# switch case
lang = input('Cual es tu lenguaje favorito?')

match lang:
    case 'JavaScript':
        print(f'Tu lenguaje favorito es {lang}')

    case 'Python':
        print(f'Tu lenguaje favorito es {lang}')