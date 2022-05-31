while True:
    print('---'*8)
    x = str(input(('Escolha um número para base de conversão:\n[1] Para binário\n[2] Para octal\n[3] Para hexadecimal\n[x] Para sair\n ')))
    if x == '1' or x == '2' or x == '3':
        if x == '1':
            bin1 = str(input('Qual número inteiro será convertido em binário?\n: '))
            if bin1.isnumeric() == True:
                print('O número inteiro {} em binário é {}'.format(bin1 ,bin(int(bin1))[2:]))
        elif x == '2':
            oct2 = str(input('Qual número inteiro será convertido em octal?\n: '))
            if oct2.isnumeric() == True:
                print('O número inteiro {} em octal é {}'.format(oct2, oct(int(oct2))[2:]))
        elif x == '3':
            hex3 = str(input('Qual número inteiro será convertido em hexadecimal?\n: '))
            if hex3.isnumeric() == True:
                print('O número inteiro {} em hexadecimal é {}'.format(hex3, hex(int(hex3))[2:]))
        else:
            print('Opção invalida')
    elif x == 'x' or x == 'X':
        break
    else:
        print('Opção invalida')