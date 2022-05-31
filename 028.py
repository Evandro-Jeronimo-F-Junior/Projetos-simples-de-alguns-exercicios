from random import randint
num = randint(0, 5)
x = int(input('Tente acertar o número aleatório de 0 a 5 que a maquina pensou.\nDigite um número: '))
if x < 6:
    if x == num:
        print('Você venceu!')
    else:
        print('Vocẽ perdeu, tente novamente!')
else:
    print('Número invalido!')
