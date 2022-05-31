#jeito que eu fiz
for i in range(1, 51):
    if i % 2==0:
        n = 0
        n += i
        print('{}'.format(n), end=' ')
print('Acabou')
# jeito que economiza processador
for num in range(2, 51, 2):
    print(num, end=' ')
print('Acabou')