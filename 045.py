print('Vamos jogar jokempô')
a = 'Papel'
b = 'Tesoura'
c = 'Pedra'
from random import randint
while True:
    x = str(input(( 'Escolha um número:\n[1]-Para papél\n[2]-Para tesoura\n[3]-Para pedra\n[x] Para sair\n '))).strip()
    n = randint(1, 3)
    if x == '1' or x == '2' or x == '3':
#Posso usar sem variáveis pra economizar memória
        if x == '1':
            x = 2
            if x<randint(1, 3):
                print('Vocẽ escolheu \033[1:33m{}\033[m\nEu escolhi \033[1:31m{}\033[m\nEu venci!'.format('Papel', 'Tesoura'))
            elif x>randint(1, 3):
                print('Vocẽ escolheu {}\nEu escolhi {}\nDroga, você venceu!'.format('Papel', 'Pédra'))
            else:
                print('Vocẽ escolheu {}\nEu escolhi {}\nEmpatamos!'.format('papel', 'Papel'))
        if x == '2':
            x = 2
            if x < randint(1, 3):
                print('Vocẽ escolheu {}\nEu escolhi {}\nEu venci!'.format(b, c))
            elif x > randint(1, 3):
                print('Vocẽ escolheu {}\nEu escolhi {}\nDroga, você venceu!'.format(b, a))
            else:
                print('Vocẽ escolheu {}\nEu escolhi {}\nEmpatamos!'.format(b, b))
# mas também posso usar as variáves
        if x == '3':
            x = 2
            if x < randint(1, 3):
                print('Vocẽ escolheu {}\nEu escolhi {}\nEu venci!'.format(c, a))
            elif x > randint(1, 3):
                print('Vocẽ escolheu {}\nEu escolhi {}\nDroga, você venceu!'.format(c, b))
            else:
                print('Vocẽ escolheu {}\nEu escolhi {}\nEmpatamos!'.format(c, c))
    elif x == 'X' or x== 'x':
        break
    else:
        print('Número inválido')
