cont = soma = 0
while True:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    soma+=n
    cont+=1
print(f'O número de tentativas foi {cont} e a soma é {soma}')
