while True:
    print('-'*40)
    print('Menu principal')
    print('-'*40)
    print(f"1 - Ver pessoas cadastradas\n2 - Cadastrar nova pessoa\n3 - Sair do sistema")
    print('-'*40)
    while True:
        try:
            a = int(input('Sua Opção: '))
        except:
            print('Digite um número válido(1, 2, 3)!')
        else:
            break
    if a == 1:
        arquivo = open('new.txt', 'r+')
        print('-='*20)
        print(arquivo.read())
        print('-='*20)
    elif a == 2:
        nome = input('Nome: ').strip().title()
        while True:
            try:
                idade = int(input('Idade: '))
            except:
                print('Digite um número válido')
            else:
                break
        arquivo = open('new1.txt', 'a+')
        arquivo.write(f"{nome:<40} {idade}\n")
    elif a == 3:
        break
    print('Erro! Digite um número válido(1, 2, 3)')
