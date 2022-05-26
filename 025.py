"""#Modo que eu fiz
x = str(input('digite seu nome completo: ')).title().split()
a = x.count('Silva')
if a == 1:
    print('Esse nome possui "Silva"')
else: print('Esse nome não possui "Silva"')"""
#modo que eu também fiz
x = str(input('digite seu nome completo: ')).title().title()
a = 'Silva' in x
print(a)
