from random import randint
from operator import itemgetter
dado = {'1': randint(1, 6), '2': randint(1, 6), '3': randint(1, 6), '4': randint(1, 6)}
for i, y in dado.items():
    print(f'O jogador {i} tirou {y}')
dado1 = sorted(dado.items(), key=itemgetter(1), reverse=True)
print('Ranking dos jogadores:')
for i in range(4):
    print(f'{i+1}° lugar: Jogador {dado1[i][0]} com {dado1[i][1]}')
