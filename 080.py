a = []
b = 0
indi = 0
maior = 0
menor = 0
b = int(input('Digite um número: '))
a.append(b)
for i in range(4):
    b = int(input('Digite um número: '))
    for indice, valor in enumerate(a):
        if maior == 0:
            maior = valor
            print('Adicionado a primeira posição.')
        elif valor < b:
            maior = valor
            indi = indice
        print(maior)
        print(a)
