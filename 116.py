a = int(input('Digite um número inteiro: '))
b = int(input('Digite outro número inteiro: '))
numero = input('digite um numero real ou uma divisão: ')
d = '/' in numero
print(d)
if d:
    numerador, denominador = numero.split('/')
    numero = int(numerador) / int(denominador)
else:
    numero = float(numero)
print(a+b+numero)
