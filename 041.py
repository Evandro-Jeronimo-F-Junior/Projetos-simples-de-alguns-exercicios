import datetime
date = str(datetime.datetime.now()).split('-')
date = date[0]
x = input('Digite seu ano de nascimento com 4 digitos').strip()
if len(x) == 4:
    x = int(date) - int(x)
    if int(x) <= 9:
        print('Mirim')
    elif 10 <= int(x) <= 14:
        print('Infantil')
    elif 15 <= int(x) < 19:
        print('Junior')
    elif int(x) == 19:
        print('Sênior')
    else:
        print('Master')