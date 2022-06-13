a = []
a.append(input('Digite uma espressão: '))
if a.count('(') == 1 and a.count(')') == 1:
    print('Sua espressão está correta')
elif a.count('(') == 1 and a.count(')') == 0:
    print('Sua expressão está errada!')
elif a.count('(') == 0 and a.count(')') == 1:
    print('Sua expressão está errada!')
else:
    if a.count(')')%2 == 1:
        print('Sua expressão está errada!')
    elif a.count('(')%2 == 1:
        print('Sua expressão está errada!')
    else:
        print('Sua espressão está correta')