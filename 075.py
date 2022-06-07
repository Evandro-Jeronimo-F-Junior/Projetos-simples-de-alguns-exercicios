t = (int(input('Primeiro número: ')), int(input('Segundo número: ')), int(input('Terceiro número: ')), int(input('Quarto número: ')), int(input('Quinto número: ')))
print('O nove apareceu {} vezes'.format(t.count(9)))
if 3 in t:
    print('primeiro valor três está na {}° pisição.'.format(t.index(3)+1))
else:
    print('Não a número 3.')
print('Os números pares são ', end='')
for n in t:
    if n%2 == 0:
        print(n, end=' ')