"""#fiz até 90° alternando
seno = {0:0, 30:0.5, 45:2**0.5/2, 60:(3**(1/2))/2, 90:1}
cosseno = {0:1, 30:(3**(1/2))/2 , 45:2**0.5/2, 60:0.5, 90:0}
tangente = {0:0 ,30:(3**(1/2))/3, 45:1, 60:3**0.5, 90:'Não existe'}
x = str(input('Digite o número dos graus para saber o seno, cosseno e a tangente: '))
if '°' in x:
    x = x.split('°')
    x = x[0]
x = int(x)
print(f'seno: {seno[x]}\ncosseno {cosseno[x]}\ntangente {tangente[x]}')"""
#modo que eu acho que ele quer
from math import tan, cos, sin, radians
x = str(input('Digite o número dos graus para o seno, cosseno e a tangente: '))
if '°' in x:
    x = x.split('°')
    x = x[0]
x = int(x)
print(f'seno: {sin(radians(x)):.2f}')
print(f'cosseno: {cos(radians(x)):.2f}')
print(f'tangente: {tan(radians(x)):.2f}')