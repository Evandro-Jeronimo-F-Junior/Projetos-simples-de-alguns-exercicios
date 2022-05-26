from math import ceil
km = ceil(float(input('Digite os kilometros percorridos: ')))
dias = float(input('Digite a quantidade de dias usados:'))
print('O valor a ser pago é {:.2f} reais'.format(km*0.15+dias*60))
