a = []
for c in range(5):
    n = int(input('D: '))
    if c == 0 or n > a[len(a)-1]:
        a.append(n)
        print('adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(a):
            if n <= a[pos]:
                a.insert(pos, n)
                print(f'adicionado a posição {pos}')
                break
            pos += 1
    print(f'Os valores digitados em ordem foram {a}')
 
