a = []
print('Digite 5 pesos e veja qual é o maior e qual é o menor')
for i in range(1, 6):
    a.append(int(input('Peso{}: '.format(i))))
print('O maior pesoo é {} e o menor peso é {}'.format(max(a),min(a)))
