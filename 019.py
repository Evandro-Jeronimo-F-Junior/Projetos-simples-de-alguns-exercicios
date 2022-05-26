from random import randint
a = str(input('Digite o primeiro nome: ')).strip().capitalize()
b = str(input('Digite o segundo nome: ')).strip().capitalize()
c = str(input('Digite o terceiro nome: ')).strip().capitalize()
d = str(input('Digite o quarto nome :')).strip().capitalize()
x = {1: a, 2: b, 3: c, 4: d}
print(f'O aluno escolhido foi {x[randint(1, 4,)]}')
"""from random import choice
a = str(input('Digite o primeiro nome: '))
b = str(input('Digite o segundo nome: '))
c = str(input('Digite o terceiro nome: '))
d = str(input('Digite o quarto nome :'))
x =(a, b, c, d)
print(choice(x))
"""