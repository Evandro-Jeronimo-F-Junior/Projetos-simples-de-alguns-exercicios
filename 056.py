#Adicionei 2 médias: uma com lista e outra com média com uma varavel simples
media = []
media1 = 0
vei = 0
nomevei = 0
senhorita = 0
senhoritaidade = 20
quantidademulher = 0
for i in range(1, 5):
    print('_____{}° Pessoa_____'.format(i))
    nome = input("Nome: ").strip().title()
    idade = int(input('Idade: '))
    sexo = input("masculino ou feminino?\nM/F: ").strip()
    media1 += idade
    media.append(idade)
    if vei < idade and sexo in 'Mm':
        vei = idade
        nomevei = nome
    if sexo in 'Ff' and idade < senhoritaidade:
        senhorita = nome
        senhoritaidade = idade
        quantidademulher += 1
if senhorita == 0:
    print('Não a mulheres com menos de 20 anos')
else:
    print('Tem {} mulheres com menos de 20 anos e a mulher mais nova é {} com {} anos'.format(quantidademulher, senhorita, senhoritaidade))
print('O mais velho é {} com {}'.format(nomevei, vei))
print('media das idades {} {}'.format(sum(media)/4, media1/4))
print(type(media1))