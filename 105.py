def nota(*a, sit=False):
    """salva alguns dados bobos sobre escola em dicionárioa"""
    dados = {}
    for i, y in enumerate(a):
        if i == 0:
            dados['maior'] = y
            dados['menor'] = y
            dados['media'] = y
        elif y > dados['maior']:
            dados['maior'] = y
        if y < dados['menor']:
            dados['menor'] = y
        if i > 0:
            dados['media'] += y
    dados['media'] = dados['media'] / (i + 1)
    dados['total'] = i+1
    if sit:
        if dados['media'] >= 7:
            dados['situaçao'] = 'aprovado'
        elif dados['media'] > 3:
            dados['situaçao'] = 'recuperação'
        else:
            dados['situaçao'] = 'reprovado'
    return dados


print(nota(5.5, 2.5, 1.5, sit=True))
help(nota)