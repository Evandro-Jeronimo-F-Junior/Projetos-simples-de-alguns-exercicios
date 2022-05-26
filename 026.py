#modo que eu fiz
x = str(input('digite uma frase: ')).lower().strip()
print('A letra a aparece {} vezes'.format(x.count('a')))
print('A Primeira letra "A" aparece na posiçao {}'.format(x.find('a') + 1))
a = x.count(' ')
print('A ultima letra "A" aparece na posiçao {}'.format(x.rfind('a') +1 - a))