a = ''
a = input().lower().strip()
while a != 'fim':
    print(f'Acessabdo manual do {a}')
    help(a)
    a = input().lower().strip()