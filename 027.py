#modo como eu fiz
x = str(input('Digite seu nome: ')).strip().title().split()
print('Seu primeiro nome é: {}'.format(x[0]))
print('Seu ultimo nome é: {}'.format(x[len(x) - 1]))
