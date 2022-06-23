def ficha(a, b):
   if a == '':
      a = "Unamed"
   if b == '':
      b = 0
   return f"Nome do jogador {a} e fez {b} gol(s)"


print(ficha(input("Nome: ").strip().title(), input(('Quantos gols você marcou?').strip())))
