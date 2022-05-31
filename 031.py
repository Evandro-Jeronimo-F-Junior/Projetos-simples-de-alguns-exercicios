print('Preço é R$0,50 por km até 200km e R$0,45 para viagens mais longas')
x = float(input('Digite a disância em km: '))
if x <= 200:
    print('O valor é da passagem é {}'.format(x*0.50))
else:
    print('O valor é da passagem é {}'.format(x*0.45))