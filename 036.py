vc = float(input('Qual o valor da casa que você quer comprar?'))
sa = float(input('qual seu salário?'))
qp = float(input('Vai pagar em quanto tempo?'))
if vc/qp >= sa*0.30*12:
    print('Esprestimo negado')
else:
    print('Emprestimo aceito, parabens!')
