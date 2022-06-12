a = []
while True:
    a.append(int(input('Digite um número')))
    if a.count(a[len(a)-1]) > 1:
        a.pop()
    if input('Quer parar? [S/N]').upper().strip() in 'N':
        continue
    else:
        print('Os valores únicos digitados são {}'.format(sorted(a)))
        break
