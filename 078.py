a = []
cont = 0
cont1 = []
cont2 = []
for i in range(5):
    a.append(int(input('Digite um valor: ')))
print(f'O máximo é {max(a)}, o mínimo é {min(a)}\nO mínimo está na posição(s)', end=' ')
for y, v in enumerate(a):
    if v == min(a):
        print(f'{y+1}°...', end=' ')
print('\nOs maiores estão nas posiçoes ', end='')
for y, v in enumerate(a):
    if v == max(a):
        print(f'{y+1}°...', end=' ')
