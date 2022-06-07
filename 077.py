a = ('e utilizado', 'para', 'alinhar ao centro', 'uma corda com a largura dada da', 'corda')
for i in range(len(a)):
    print ('Na palavra [{}] temos:'.format(a[i].upper()), end=' ')
    for y in a[i].lower():
        if y=='a' or y=='e' or y=='i' or y=='o' or y=='u':
            print(y,end=' ')
    print()