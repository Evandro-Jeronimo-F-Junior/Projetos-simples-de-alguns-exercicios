x = int(input('Para saber se o ano é bissexto digite o ano: '))
if x % 4 == 0:
    print('O ano de {} é um ano bissexto'.format(x))
else:
    print('O ano {} não é bissexto'.format(x))
