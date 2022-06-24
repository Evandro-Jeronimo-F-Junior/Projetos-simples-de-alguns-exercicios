def dobro(b, format=False):
    res = b*2
    return res if format == False else moeda(res)


def metade(a, format=False):
    res = a/2
    return res if format == False else moeda(res)


def moeda(a, b = 'R$'):
    return f"{b}{a:.2f}".replace('.', ',')

