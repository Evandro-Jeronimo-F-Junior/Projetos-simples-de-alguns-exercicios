#forma que eu fiz
"""x = int(input('Digite um número de 0 a 9999: '))
if x <= 9999:
    a = x // 1000
    b = x - a * 1000
    b_r = b // 100
    c = b - b_r * 100
    c_r = c // 10
    d = c - c_r * 10
    d_r = d // 1
    print('unidade:{}\ndezena:{}\ncentena:{}\nmilhar:{} '.format(d_r, c_r, b_r, a).title())
else: print('Número não aceito')

#modo strings mas não serve
x = str(input('Digite um número de 0 a 9999: '))
unidade = x[3]
dezena = x[2]
centena = x[1]
milhar = x[0]
print('unidade:{}\ndezena:{}\ncentena:{}\nmilhar:{} '.format(unidade, dezena, centena, milhar).title())"""
#forma melhor
x = int(input('Digite um número de 0 a 9999: '))
if x <= 9999:
    unidade = x % 10
    dezena = x // 10 % 10
    centena = x // 100 % 10
    milhar = x // 1000
    print('unidade:{}\ndezena:{}\ncentena:{}\nmilhar:{} '.format(unidade, dezena, centena, milhar).title())
else: print('Número não aceito')
