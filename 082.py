l1 = []
l2 = []
l3 = []
while True:
    l1.append(int(input('Digite um número: ')))
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
for i in l1:
    if i%2 == 0:
        l2.append(i)
    else: l3.append(i)
print(f'{l1} os pares {l2} e os impáres {l3}')