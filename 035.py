l1 = float(input('Digite um lado: '))
l2 = float(input('Digite outro lado: '))
l3 = float(input('Digite o ultimo lado: '))
if l2+l3 > l1 > abs(l2-l3) or l1+l3 > l2 > abs(l1-l3) or l2+l1 > l3 > abs(l2-l1):
    print('Da pra formar um triangulo')
else:
    print('Não da pra formar um triangulo')
