def cont(a, b, c):
    from time import sleep
    if c == 0:
        c = 1
    if c < 0:
        c *= -1
    print(f"contagem de {a} até {b} de {abs(c)} em {abs(c)}")
    while a < b:
        sleep(0.5)
        print(a, end=' ')
        a += c
        if a == b+c:
            print('Fim!')
    while a >= b:
        sleep(0.5)
        print(a, end=' ')
        a -= c
        if a == b-c:
            print('Fim!')


cont(1, 10, 1)
cont(10, 0, 2)
print("\nAgora é sua vez de personalizar a contagem!")
cont(int(input('Inicio: ')), int(input('Vai até: ')), int(input('Passo: ')))
