cont = 1
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    while True:
        print('{}x{:2}={}'.format(n, cont, n*cont))
        cont +=1
        if cont == 11:
            cont = 1
            break
