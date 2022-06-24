import moeda
p = float(input('difite o preço: R$'))
print(f"A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p)[0])}")
print(f"O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p)[0])}")
print(f"Aumentando 10% de {moeda.moeda(p)}, temos {moeda.moeda(moeda.porcent(p, 10))}")
print(f"Reduzindo 13% de {moeda.moeda(p)}, temos {moeda.moeda(moeda.porcent(p, -13))}")
