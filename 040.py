print('Digite 4 notas para saber a média.')
n1 = float(input('Nota1: '))
n2 = float(input('Nota2: '))
n3 = float(input('Nota3: '))
n4 = float(input('Nota4: '))
if (n1+n2+n3+n4)/4 < 5:
    print('Média {}. O aluno está reprovado.'.format((n1+n2+n3+n4)/4))
elif 6.9 >=(n1+n2+n3+n4)/4 >= 5.0:
    print('Média {}. O aluno está de recuperação.'.format((n1+n2+n3+n4)/4))
else:
    print('Média {}. O aluno passou'.format((n1+n2+n3+n4)/4))
