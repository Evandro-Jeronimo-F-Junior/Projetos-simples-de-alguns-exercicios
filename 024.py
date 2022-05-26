"""#Modo que eu fiz com if
x = str(input('digite seu nome completo: ')).title().strip
a = x.find('Santo')
if a == 0:
    print('O nome começa com Santo')
else: print('O nome não começa com Santo')

x = str(input('digite seu nome completo: ')).title()
a = x.find('Santo')""""""
#modo que também fiz
x = str(input('Digite o nome de uma cidade: ')).title().strip()
b = x.split()
c = 'Santo' in b[0]
print (c)
#modo que ele fez"""
x = str(input('Digite o nome de uma cidade: ')).title().strip()
print(x[:5] == 'Santo')