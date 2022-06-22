lista = list()


def sorteia(a):
    from random import randint
    for i in range(5):
        a.append(randint(0, 10))
    return a

def somaPar(b):
    a = 0
    for y in lista:
        if y % 2 == 0:
            a += y
    return a


print("Sorteando 5 valores da lista: {0} Pronto!"
      "\nSomando os valores pares de {0}, temos {1}".format(sorteia(lista), somaPar(lista)))
