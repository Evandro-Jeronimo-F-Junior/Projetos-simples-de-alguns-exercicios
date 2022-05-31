print('Todos os funcionários receberam aumento de 10% ou 15%')
x = float(input('Digite seu salario: '))
if x > 1250:
    print('Seu é de 10% ficando em {}'.format(x+x*0.10))
else:
    print('Seu é de 15% ficando em {}'.format(x+x*0.15))
