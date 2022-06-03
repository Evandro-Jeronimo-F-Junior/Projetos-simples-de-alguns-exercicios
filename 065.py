stop = ''
media = maior = menor = cont = 0
n = ()
while not 'N' in stop:
    n = int(input('Digite um número: '))
    media += n
    cont += 1
    if n > maior:
        maior = n
    if menor == 0:
        menor = n
    if n < menor:
        menor = n
    stop = input('Quer continuar? [S/N]').strip().upper()
print('A média é {}, o maior é {} e o monor é {}'.format(media/cont, maior, menor))
