from _datetime import datetime
informaçao = dict()
informaçao['nome'] = input('Nome: ').strip().capitalize()
data = str(datetime.now()).split('-')
nascimento = input('Escreva seu ano de nascimento com 4 digitos: ').strip()
mes = input('Mês: ')
if len(nascimento) == 4 and nascimento.isnumeric() == True:
    if data[1][1] > mes:
        informaçao['idade'] = abs(int(data[0]) - int(nascimento))
        print(informaçao)
    else:
        informaçao['idade'] = abs(int(data[0]) - int(nascimento)-1)
        print(informaçao)
informaçao['ctps'] = input('Carteira de trabalho: (0 se não tiver): ')
if informaçao['ctps'] == '0':
    print(f'Seu nome é {informaçao["nome"]}\n'
          f'Sua idade é {informaçao["idade"]}\n'
          f'Não possui CTPS')
else:
    informaçao['contrataçao'] = input('Ano de contratação: ')
    informaçao['salario'] = input('Seu salário R$: ')
    print(f'Seu nome é {informaçao["nome"]}\n'
          f'Sua idade é {informaçao["idade"]}\n'
          f'Sua CTPS é {informaçao["ctps"]}\n'
          f'Ano de contratação {informaçao["contrataçao"]}\n'
          f'Salário R$:{informaçao["salario"]}\n'
          f'Você vai se aposentar aos {int(informaçao["contrataçao"]) - int(nascimento)+35}')
