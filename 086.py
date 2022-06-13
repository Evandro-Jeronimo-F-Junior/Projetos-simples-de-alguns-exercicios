a = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(3):
     for l in range(3):
          a[i][l] = int(input())
for i in range(3):
     for l in range(3):
           print(f'[{a[i][l]:^5}]', end='')
     print()
