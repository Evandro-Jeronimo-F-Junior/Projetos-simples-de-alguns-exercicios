print('Digite os lados para saber se ele é equilátero, isósceçes oou escaleno')
a = float(input('Digite o primeiro lado: '))
b = float(input('Digite o segundo lado: '))
c = float(input('Digite o terceiro lado: '))
if abs(c - b) < a < b + c and abs(a - c) < b < a + c and abs(a - b) < c < a + b:
    if a == b and b == c:
        print('Este triangulo é equilátero')
    elif a == b and a != c or b == c and b != a or c == a and c != b:
        print('Este triangulo é isósceles')
    else:
        print('Este triangulo é escaleno')
else:
    print('Não forma um triangulo')
