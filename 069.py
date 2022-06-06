ci = h = m20 = 0
while True:
    i = int(input('idade: '))
    if i > 18: ci+=1
    s = input('sexo M/F: ').strip().upper()
    if s in 'M': h+=1
    if s in 'F' and i < 20: m20+=1
    if input('Quer continuar? S/N: ').strip().upper() in 'SIM':
        continue
    else:
        print(f'Tem {ci} com mais de 18 anos, foram cadastrados {h} homens e tem {m20} mulher(s) abaixo dos 20 anos.')
        break