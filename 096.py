def area(a, b):
    print(f"A área do terreno {a}x{b} é {a * b}m²")


print(f'controle de terrenos\n{"-"*30}')
area(int(input('Largura (m): ')), int(input('Comprimento (m): ')))