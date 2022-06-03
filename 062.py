n = int(input('Digite um número: '))
r = int(input('Digite a razão: '))
c = 10
while c > 0:
    print('{}'.format(n))
    n += r
    c -= 1
    if c == 0:
        t = input('Quer adicionar mais termos?\n[S/N]: ').strip()
        if t in 'sS':
            t = int(input('Quantos mais? '))
            c = t
"""n = int(input('Digite um número: '))
r = int(input('Digite a razão: '))
c = 10
total = 0
while total > 0:
    total = c
    while c > 0:
        print('{}'.format(n))
        n += r
        c -= 1
        if c == 0:
            t = input('Quer adicionar mais termos?\n[S/N]: ').strip()
            if t in 'sS':
                t = int(input('Quantos mais? '))
                c = t"""