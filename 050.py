#Soma os pares de um conjunto de números
s=0
b=[]
c=[]
for i in range(1, 7):
    a = int(input('Digite um número para que seja somado os pares: '))
    c.append(a)
    for x in range(1, a+1):
        if x % 2==0:
            b.append(x)
            s += x
print(" A soma dos pares de {} que são {} é {}".format(c, b, s))
