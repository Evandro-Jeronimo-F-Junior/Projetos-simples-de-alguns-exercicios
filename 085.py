a = [[], []]
b = 0
for i in range(7):
    b = int(input(f'Digite o {i+1}° número: '))
    if b%2 == 0:
        a[1].append(b)
    else:
        a[0].append(b)
print(f'Par: {sorted(a[1])}\nImpar: {sorted(a[0])}')