a = ('Lápis', '1.75', 'borracha', '2.00', 'caderno', '15.90', 'estojo', '25.00', 'transferidor', '4.20')
for i in range(len(a)):
    if i%2 == 0:
        print(a[i].ljust(25, '-'), 'R$', end=' ')
    if i%2 == 1:
        print(a[i])
