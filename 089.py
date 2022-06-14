a = [[[]]]
cont = 0
while True:
    a.append(input('Nome: ').strip().title())
    a[0].append(float(input('Digite a 1° nota: ')))
    a[0][0].append(float(input('Digite a 2° nota: ')))
    while not 'N' == b:
        b = input('Quer continuar? [S/N]').strip().upper()
        if b == 'S':
            break
        elif b == 'N':
            print('-=' * 14)
            print(f'N° Nome {"Média":>8}')
            print('_'*28)
            for i in range(len(a[1:])):
                print(f'{i:<4} {a[1+i]}{(a[0][i+1]+a[0][0][i])/2:8.1f}.')
            while cont != 999:
                cont = int(input('Digite a númeração para saber as notas individualmente: '
                                 'ou 999 para parar: '))
                if cont == 999:
                    break
                else:
                    for i in range(len(a[1:])):
                        if cont == i:
                            print('{}:\nPrimeira nota: {}\nSegunda nota: {}'.format(a[i+1], a[0][i+1], a[0][0][i]))
            break
        else:
            print('Letra inválida')
    if 'N' in b:
        break
