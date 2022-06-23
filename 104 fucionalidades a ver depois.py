def leiaint(a):
    while True:
        print(a, end='')
        b = input()
        if type(b) == str:
            if b.isnumeric():
                break
        print('Erro!')
    return b


n = leiaint('Digite um número: ')