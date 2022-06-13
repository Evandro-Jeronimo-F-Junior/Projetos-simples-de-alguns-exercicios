from random import randint
a = []
b = cont = 0
c = int(input('Quantos números você quer? '))
while c != cont:
    a.append([])
    for i in range(6):
        a[cont].append(randint(1, 60))
    a[cont].sort()
    for indice, valor in enumerate(a[cont]):
        if b == valor:
            del(a[cont])
            c += 1
            a.append([])
            break
        else:
            b = valor
    if not a[cont]:
        pass
    else:
        print(a[cont])
    cont += 1
