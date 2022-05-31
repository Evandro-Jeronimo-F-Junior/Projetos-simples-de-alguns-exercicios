altura = str(input('Digite sua altura para saber seu imc: ')).strip()
peso = float(input('Digite seu peso em kg: '))
if len(altura) == 4:
    if peso / float(altura) ** 2 < 18.5:
        print('Abaixo do peso')
    elif 25 > peso / float(altura) ** 2 >= 18.5:
        print('Peso ideal')
    elif 30 > peso / float(altura) ** 2 >= 25:
        print('Sobrepeso')
    elif 40 > peso / float(altura) ** 2 >= 30:
        print('Obesidade')
    else:
        print('Obesidade mórbida')
if len(altura) == 3:
    if peso / (float(altura)/100) ** 2 < 18.5:
        print('Abaixo do peso')
    elif 25 > peso / (float(altura)/100) ** 2 >= 18.5:
        print('Peso ideal')
    elif 30 > peso / (float(altura)/100) ** 2 >= 25:
        print('Sobrepeso')
    elif 40 > peso / (float(altura)/100) ** 2 >= 30:
        print('Obesidade')
    else:
        print('Obesidade mórbida')
else:
    print('Número invalido')
