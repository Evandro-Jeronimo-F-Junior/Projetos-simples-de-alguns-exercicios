"""#modo que eu fiz
while True:
    print('[1] soma'.title())
    print('[2] multiplicar'.title())
    print('[3] Maior')
    print('[4] Sair do programa')
    a = input('Digite um número: ')
    soma = 0
    multiplicador = 0
    multiplicador1 = 0
    total = 0
    maior = ''

    if a == '1':
        for i in range(1, int(input('Quantos números você quer somar?\n: '))+1):
            soma += float(input(f'Digite o {i}° número: '))
    if soma > 0:
        print(soma)
    if a =='2':
        for i in range(1, int(input('Faça uma multiplicação ou some varias delas\nDigite o número de multiplicações: '))+1):
            multiplicador = float(input(f'Digite o {i}° número: '))
            multiplicador1 = float(input(f'Digite o {i+1}° número: '))
            total += multiplicador1 * multiplicador
            print('Resultado {}'.format(multiplicador1 * multiplicador))
    if total > 0:
        print(f'O total das somas da multiplicação é {total}')
    if a == '3':
        for i in range(1, int(input('quer saber qual é o maior entre quantos números?\n: '))+1):
            maior += input(f'Digite o {i}° número: ')
    if maior != '':
        print('O maior é {}'.format(max(maior)))
    if a == '4':
        break"""
a = ''
while a != '4':
    print('[1] soma'.title())
    print('[2] multiplicar'.title())
    print('[3] Maior')
    print('[4] Sair do programa')
    a = input('Digite um número: ')
    soma = 0
    multiplicador = 0
    multiplicador1 = 0
    total = 0
    maior = ''

    if a == '1':
        for i in range(1, int(input('Quantos números você quer somar?\n: ')) + 1):
            soma += float(input(f'Digite o {i}° número: '))
    if soma > 0:
        print(soma)
    if a == '2':
        for i in range(1, int(input(
                'Faça uma multiplicação ou some varias delas\nDigite o número de multiplicações: ')) + 1):
            multiplicador = float(input(f'Digite o {i}° número: '))
            multiplicador1 = float(input(f'Digite o {i + 1}° número: '))
            total += multiplicador1 * multiplicador
            print('Resultado {}'.format(multiplicador1 * multiplicador))
    if total > 0:
        print(f'O total das somas da multiplicação é {total}')
    if a == '3':
        for i in range(1, int(input('quer saber qual é o maior entre quantos números?\n: ')) + 1):
            maior += input(f'Digite o {i}° número: ')
    if maior != '':
        print('O maior é {}'.format(max(maior)))
