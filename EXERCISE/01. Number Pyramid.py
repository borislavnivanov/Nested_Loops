numbers = int(input())

current_n = 0
is_break = False

for row in range(numbers):
    for colum in range(row + 1):
        current_n += 1
        if current_n > numbers:
            is_break = True
            break
        else:
            print(f'{current_n}', end=' ')

    if is_break:
        break
    else:
        print('')
