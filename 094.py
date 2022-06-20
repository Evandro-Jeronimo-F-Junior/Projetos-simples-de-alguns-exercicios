lista = list()
dados = dict()
mulheres = list()
idade = list()
mediatotal = 0
while True:
    dados['Nome'] = input('Nome: ').strip().title()
    dados['Idade'] = input('Idade: ').strip()
    while True:
        dados['Sexo'] = input('Sexo: [M/F]').upper().strip()[0]
        if dados['Sexo'] in 'FM':
            break
        print('Erro! porfavor digite apenas M ou F.')
    lista.append(dados.copy())
    while True:
        a = input('Quer continuar? [S/N] ').strip().upper()[0]
        if a in 'NS':
            break
        print('Erro . Porfavor digite apenas S ou N.')
    if a == 'N':
        print(f'Foram cadastradas {len(lista)} pessoa(s)')
        for i in range(len(lista)):
            if lista[i]['Sexo'] == 'F':
                mulheres.append(lista[i]["Nome"])
            mediatotal += int(lista[i]['Idade'])
        for i in range(len(lista)):
            if mediatotal / len(lista) < int(lista[i]['Idade']):
                idade.append(lista[i]['Nome'])
        print(f'A média de idade do grupo é {mediatotal / len(lista)} anos.')
        print('As mulheres são: ', end='')
        for i in range(len(mulheres)):
            print(f'{mulheres[i]},', end=' ')
        print()
        print('As pessoas com idade acima da média são: ', end=' ')
        for i in range(len(idade)):
            print(f'{idade[i]},', end=' ')
        break
