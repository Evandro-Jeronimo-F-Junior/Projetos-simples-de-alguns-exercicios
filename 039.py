import datetime
data = str(datetime.datetime.now()).split('-')
nascimento = input('Escreva seu ano de nascimento com 4 digitos: ').strip()
if len(nascimento) == 4 and nascimento.isnumeric() == True:
    if int(data[0]) - 18 == int(nascimento):
        print('Você tem que se alistar este ano')
    elif int(data[0]) - 18 > int(nascimento):
        print('Já passou seu ano de alistamento')
    elif int(data[0]) - 18 < int(nascimento):
        print('Ainda não é seu ano de alistamento faltam {} ano(s).'.format(int(nascimento) - int((data[0])) + 18))
else:
        print('Número invalido')
