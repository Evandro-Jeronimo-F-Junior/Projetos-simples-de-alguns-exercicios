n1 = int(input('Digite o primeiro termo: '))
n2 = int(input('Digite a razão: '))
for i in range(n1, n1+10*n2, n2):
    print(i)
#só de palhaçada o msm código em 2 linhas:
for i in range(int(input('Digite o primeiro termo: ')), int(input('Digite o primeiro termo novamene: '))+10*int(input('Digite a razão: ')), int(input('Digite a razão novamente: '))):
    print(i)