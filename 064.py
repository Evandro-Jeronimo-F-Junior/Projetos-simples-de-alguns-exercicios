n = c = n1 = 0
n = int(input('Para parar digite o número 999: '))
while n != 999:
   c+=1
   n1+=n
   n = int(input('Para parar digite o número 999: '))
print(f'O número de tentativas foi {c} e a soma é {n1}')
