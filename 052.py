n1 = abs(int(input('Digite um número para saber se ele é primo: ')))
n2=0
for i in range(1, n1+1):
    if n1%i==0:
        n2+= 1
if n2 >= 3:
    print('Não é primo')
else:
    print('É primo')