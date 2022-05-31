s = 0
a = 0
for i in range(1, 501, 2):
    s+=i
    if i%2 == 1:
        a+=1
print('O número 500 tem {} números impares e a soma deles é {}'.format(a, s))
"""#Vou fazer uma brincadeira
npares = 0
nimpares = 0
somapares = 0
somaimpares = 0
for i in range(1, int(input('Digite umm número para ver seus pares, impares e suas somas'))):
    if i%2 == 0:
        npares+=1
        somapares+=i
    if i%2 == 1:
        nimpares+=1
        somaimpares+=i
print('Tem {} números pares e a soma deles é {}'.format(npares, somapares))
print('Tem {} números impares e a soma deles é {}'.format(nimpares, somaimpares))"""