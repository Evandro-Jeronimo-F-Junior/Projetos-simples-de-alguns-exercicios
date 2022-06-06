"""cont = 0
t = 0
pmb = ''
ini = 0
while True:
    n = input('Nome: ')
    p = int(input('Preço: '))
    t+=p
    if p > 1000: cont+=1
    if pmb == '':
        pmb = n
        ini = p
    if ini > p:
        pmb = n
    if input('Quer continuar? [S/N]').strip().upper() in 'SIM':
        continue
    else:
        print(f'O total gasto é {t}, {cont} produtos custam mais que 1000 reais e o produto mais barato é {pmb}.')"""
cont = 0
t = 0
pmb = ''
ini = 0
c = ''
while True:
    n = input('Nome: ')
    p = int(input('Preço: '))
    t+=p
    if p > 1000: cont+=1
    if pmb == '':
        pmb = n
        ini = p
    if ini > p:
        pmb = n
    while True:
        c = input('Quer continuar? [S/N]').strip().upper()
        if c in "SIM":
            break
        elif c in "NÃO":
            print(f'O total gasto é {t}, {cont} produtos custam mais que 1000 reais e o produto mais barato é {pmb}.')
            break
        else:
            print('Número inválido')
    if c in "NÃO":
        break