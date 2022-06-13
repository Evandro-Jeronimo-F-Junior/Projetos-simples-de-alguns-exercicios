l = [[], []]
print('Quando quiser parar digite [X]')
while True:
    l[0].append(input('Nome: ').strip().capitalize())
    if l[0][-1] == 'X':
        l[0].pop()
        break
    l[1].append(input('Peso: ').strip().upper())
    if l[1][-1] == 'X':
        l[0].pop()
        l[1].pop()
        break
    else:
        l[1][-1] = float(l[1][-1])
print(f'Vocẽ cadastrou {len(l[0])} pessoas')
print(f'O maior peso foi de {max(l[1])}. Peso de ', end='')
for i, y in enumerate(l[1]):
    if y == max(l[1]):
        print(f'{l[0][i]}.', end=' ')
print(f'\nO menor peso foi de {min(l[1])}. Peso de',end=' ')
for i, y in enumerate(l[1]):
    if y == min(l[1]):
        print(f'{l[0][i]}.', end=' ')
