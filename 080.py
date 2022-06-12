a = []
a.append(int(input('Digite um número: ')))
print('Foi adicionado a primeira posiçao')
b = 0
for i in range(4):
    b = int(input('Digite um número: '))
    if b > max(a):
        print(f'Adicionado na posição {a.index(max(a))+1}')
        a.insert(a.index(max(a))+1, b)
    elif b < min(a):
        print(f'Adicionado na posição {a.index(min(a))}')
        a.insert(a.index(min(a)), b)
print(a)
