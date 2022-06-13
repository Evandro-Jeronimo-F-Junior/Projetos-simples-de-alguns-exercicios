a = []
b = 0
while True:
    b = int(input('Digite um número qualquer: '))
    if not a or a[0] < b:
        a.insert(0, b)
    else:
        for i in range(len(a)-1, -1, -1):
            if b < a[i]:
                a.insert(i+1, b)
                break
    b = ''
    while True:
        b = input('Quer continuar? [S/N] ')
        if b in 'Nn':
            break
        elif b in 'Ss':
            break
        else:
            print('Você digitou errado tente novamente')
    if b in 'Nn':
        break
print(f'foram digitados {len(a)} vezes, e a lista é: {a}', end='')
if a.count(5) == 1:
    print(f' o 5 está na lista na posição {a.index(5)}')
else:
    print(' não a número(s) 5')