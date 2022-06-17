dados = dict()
dados['Nome'] = input('Nome: ').strip().title()
dados['Partidas'] = input('Quantas partidas você jogou? ')
dados['Total de gols'] = 0
for i in range(int(dados['Partidas'])):
    dados['Total de gols'] += int(input(f'Gol(s) na {i+1}° partida(s): '))
print(dados)
for i, y in dados.items():
    print(f'{i}: {y}')
