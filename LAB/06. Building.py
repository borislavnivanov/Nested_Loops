flour = int(input())
rooms = int(input())

for i in range(flour, 0, -1):
    for r in range(rooms):
        if i == flour:
            print(f'L{i}{r}', end=' ')
        elif i % 2 == 0:
            print(f'O{i}{r}', end=' ')
        else:
            print(f'A{i}{r}', end=' ')
    print('')
