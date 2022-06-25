def leiaint(a=0):
    while True:
        try:
            b = int(input('Digite um número inteiro: '))
        except (ValueError, TypeError):
            print("Erro digite um número inteiro!")
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuário')
        else:
            break
    return b


def leiafloat(a=0):
    while True:
        try:
            b = float(input('Digite um número real: '))
        except (ValueError, TypeError):
            print("Erro digite um número inteiro!")
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuário')
        else:
            break
    return b

n1 = leiaint()
n2 = leiafloat()
print(f"O valor inteiro digitado foi {n1} e o valor real foi {n2}")
