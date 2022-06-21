b = list()
while True:
    a = {'Nome': input("Nome: ").title().strip(), 'Gols': []}
    for i in range(0, int(input('Quantas partidas você jogou? '))):
        a['Gols'].append(int(input(f'quantos gols você fez na {i+1}° partida: ')))
    a['Partidas'] = i+1
    b.append(a.copy())
    while True:
        x = input('Quer continuar? [S/N] ').upper().strip()[0]
        if x in 'NS':
            break
        print("Erro! digite S ou N")
    if x in 'N':
        print('-='*30)
        print(f"{'cod':>0} {'nome':>1} {'gols':>18} {'total':>21}")
        print('-'*48)
        break
for i in range(0, len(b), 1):
    print(f"{i:>3} {b[i]['Nome']:<20}", end='')
    print("{:<20}".format("{}".format(b[i]['Gols'])), end='')
    print(f"{sum(b[i]['Gols'])}")
print('-'*48)
while i != 999:
    i = int(input('Mostrar os dados de qual jogador? (999 para parar) '))
    if i >= len(b):
        print("Erro! não existe este jogador")
    else:
        print(f"-- Levantamento do jogador {b[i]['Nome']}")
        for x in range(0, len(b[i]['Gols'])):
            print(f"No jogo {x+1} fez {b[i]['Gols'][x]} gol(s)")
