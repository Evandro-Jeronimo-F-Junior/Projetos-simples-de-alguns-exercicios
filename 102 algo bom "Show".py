def fat(a=1, show=False):
    b = 1
    for i in range(a, 0, -1):
        b *= i
        if show:
            print(i, end=' ')
            if i > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
    return b


print(fat(int(input('Digite um número para saber o factorial dele')), bool(int(input('Quer que mostre a conta? (0 para não)')))))