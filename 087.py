a = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma3 = somap = maior = 0
for i in range(3):
    for l in range(3):
        a[i][l] = int(input())
for i in range(3):
    for l in range(3):
        if i == 1:
            if maior == 0:
                maior = a[i][l]
            elif maior < a[i][l]:
                maior = a[i][l]
        if l == 2:
            soma3 += a[i][l]
        if a[i][l] % 2 == 0:
            somap += a[i][l]
        print(f'[{a[i][l]:^5}]', end='')
    print()
print(f'a soma de todos os valores pares é {somap}'
      f'\nA soma dos valors da terceira coluna é {soma3}'
      f'\nO maior valor da segunda linha é {maior}')
