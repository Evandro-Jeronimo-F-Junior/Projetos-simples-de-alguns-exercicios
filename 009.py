"""#modo que eu fiz pra testar
x = int(input('Digite um número para ver a tabuada: '))
print('{0}x1={1}\n{0}x2={2}\n{0}x3={3}\n{0}x4={4}\n{0}x5={5}\n{0}x6={6}\n{0}x7={7}\n{0}x8={8}\n{0}x9={9}\n{0}x10={10}'.format(x, x*1, x*2, x*3, x*4, x*5, x*6, x*7, x*8, x*9, x*10))"""
num = int(input('Digite um número para ver sua tabuada: '))
print('-'*13)
print('{} x {:2} = {}'.format(num, 1, num*1))
print('{} x {:2} = {}'.format(num, 2, num*2))
print('{} x {:2} = {}'.format(num, 3, num*3))
print('{} x {:2} = {}'.format(num, 4, num*4))
print('{} x {:2} = {}'.format(num, 5, num*5))
print('{} x {:2} = {}'.format(num, 6, num*6))
print('{} x {:2} = {}'.format(num, 7, num*7))
print('{} x {:2} = {}'.format(num, 8, num*8))
print('{} x {:2} = {}'.format(num, 9, num*9))
print('{} x {:2} = {}'.format(num, 10, num*10))
print('-'*13)
