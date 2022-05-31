"""#para ver se é um palíndromo

a = input().strip().lower()
a = a.split(' ')
a = ('').join(a)
b = a[::-1]
if a == b:
    print('A frase é um palíndromo')
else:
    print('Não é um palíndromo')"""
a = str(input().strip().lower())
a = a.split(' ')
a = ('').join(a)
b = ''
for i in range(len(a)-1 , -1, -1):
    b += a[i]
if b == a:
    print('A frase é um palíndromo')
else:
    print('Não é um palíndromo')
