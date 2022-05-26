import math
largura = float(input('Escreva a largura em números: '))
altura = float(input('Escreva a altura em números: '))
print('Você irá precisar de {} latas de tinta'.format(math.ceil(largura*altura/2)))
