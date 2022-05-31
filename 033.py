print('Escreva 3 números para saber qual é o maior e qual é o menor')
x = float(input('Digite um número: '))
a = float(input('Digite um número: '))
b = float(input('Digite um número: '))
if x > a and x > b:
    print('O numero {} é o maior'.format(x))
if a > x and a > b:
    print('O numero {} é o maior'.format(a))
if b > x and b > a:
    print('O numero {} é o maior'.format(b))
if x < a and x < b:
    print('O numero {} é o menor'.format(x))
if a < x and a < b:
    print('O numero {} é o menor'.format(a))
if b < x and b < a:
    print('O numero {} é o menor'.format(b))
