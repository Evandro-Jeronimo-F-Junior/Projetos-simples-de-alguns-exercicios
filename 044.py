a = float(input('Valor: '))
print('Para saber os valores de pagamento digite:\n[1]-Dinheiro ou cheque\n[2]-Cartão á vista\n[3]-2 Vezes no cartão\n[4]-3 Vezes no cartão ou mais')
x = input(': ').strip()
if x == '1':
      print('De R${} por R${}\n10% de desconto.'.format(a, a-a*0.10))
elif x == '2':
      print('De R${} por R${}\n5% de desconto.'.format(a, a-a*0.05))
elif x =='3':
      print('Preço normal R${}.'.format(a))
elif x == '4':
      print('De R${} por R${}Com 20% de acréscimo.'.format(a, a+a*0.20))
else:
      print('Número errado')
