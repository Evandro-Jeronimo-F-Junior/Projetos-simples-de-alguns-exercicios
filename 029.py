print('Limite de velocidade é 80km/h, acima disto a uma multa de R$7,00 por cada km acima do limite')
x = int(input('Digite a velocidade: '))
if x <= 80:
    print('Não a multa')
else:
    print('Multa de R${}'.format((x - 80)*7))
