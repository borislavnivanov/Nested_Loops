n = int(input())

for a in range(2):
    print('+', end=' ')
    for _ in range(n - 2):
        print('-', end=' ')
    print('+', end='\n')

    if a == 0:
        for i in range(n - 2):
            print('|', end=' ')
            for _ in range(n - 2):
                print('-', end=' ')
            print('|', end='\n')
