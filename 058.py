from random import randint
a = 0
b = -1
c = 0
print('Digite um número de 1 a 10 para tentar adivinhar o número que pensei')
while a != b:
    a = randint(1, 10)
    b = int(input('Número: '))
    c += 1
else: print('venceu com {} tentativas'.format(c))
