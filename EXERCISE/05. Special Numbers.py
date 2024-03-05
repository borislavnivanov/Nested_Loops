number = int(input())
special_numbers = []

for i in range(1111, 10000):
    count = 0

    for f, digit in enumerate(str(i)):
        if int(digit) == 0:
            continue
        if number % int(digit) == 0:
            count += 1

    if count == 4:
        special_numbers.append(i)

for i in range(len(special_numbers)):
    print(f'{special_numbers[i]}', end=' ')
