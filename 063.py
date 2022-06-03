n = int(input('Quantos termos você quer mostrar: '))
i = [0, 1]
c = 0
while n-2 >= c:
    i.append(sum((i[-2:])))
    print(i[c], end='-')
    c+=1
print('{}'.format(i[c]), end='')
print('-FIM')
