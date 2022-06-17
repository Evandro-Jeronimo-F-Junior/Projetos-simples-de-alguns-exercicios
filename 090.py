a = {'nome': input('Nome: '), 'media': float(input('Digite sua média: '))}
print(f'Seu nome é {a["nome"]}\nSua média é {a["media"]}')
if a['media'] >= 7:
    print('Você passou')
elif a['media'] > 3:
    print('Recuperação')
else:
    print('Reprovado')
