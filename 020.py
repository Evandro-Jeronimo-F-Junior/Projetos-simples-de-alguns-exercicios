from random import shuffle
a = str(input('Digite o primeiro nome: ')).strip().capitalize()
b = str(input('Digite o segundo nome: ')).strip().capitalize()
c = str(input('Digite o terceiro nome: ')).strip().capitalize()
d = str(input('Digite o quarto nome :')).strip().capitalize()
x = [a, b, c, d]
shuffle(x)
print(f'A ordem de trabalhos será: {x}')