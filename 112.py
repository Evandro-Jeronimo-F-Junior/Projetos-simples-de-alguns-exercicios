import moeda
p = moeda.leiadinheiro('Digite um preço')
for i in p:
    if i in ',':
        p = p.replace(',', '.')
        p = float(p)
p = float(p)
print(f"{p} não é um preço!")
print(moeda.resumo(p, 35, 22))
