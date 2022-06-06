from random import randint
cont = 0
while True:
    if input('Digite par ou impar: ').strip().upper() in 'PAR' :
        n2 = randint(1, 2)
        n = int(input('Digite um número: '))
        if (n2+n)%2 == 0:
            cont += 1
            print('Você ganhou ')
        else:
            print(f'Você perdeu\nVitórias consecutivas [{cont}]')
            break
    else:
        n2 = randint(1, 2)
        n = int(input('ava: '))
        if (n2 + n) % 2 != 0:
            print('Você ganhou')
            cont += 1
        else:
            print(f'Você perdeu\nVitórias consecutivas [{cont}]')
            break