def aumentar(* a):
    b = 0
    for i in a:
        b += i
    return b


def diminuir(* a):
    b = 0
    for i, y in enumerate(a):
        if i == 0:
            b = y
        else:
            b -= y
    return b


def dobro(* a):
    b = list()
    for i in a:
        b.append(2*i)
    return b


def metade(* a):
    b = list()
    for i in a:
        b.append(i/2)
    return b

def porcent(a, b):
    b /= 100
    a = a + (a*b)
    return a


def moeda(a, b = 'R$'):
    return f"{b}{a:.2f}".replace('.', ',')


def resumo(a=0, b=0, c=0):
    return f"{'-'*30}\n{'Resumo do valor':^30}\n{'-'*30}\n" \
           f"{'Preço analisado:':<25} {moeda(a):<13}\n" \
           f"{'Dobro do preço:':<25} {moeda(dobro(a)[0]):<13}\n" \
           f"{'Metade:':<25} {moeda(metade(a)[0]):<13}\n" \
           f"{b:>2}{'% de aumento:':<23} {moeda(porcent(a, b)):<13}\n" \
           f"{c:>2}{'% de redução':<23} {moeda(porcent(a, -c)):<13}\n{'-'*30}"

def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = input(msg).strip()
        if entrada.isalpha():
            print('Preço invalido')
        else:
            return entrada
            valido = True

