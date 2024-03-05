n1 = int(input())
n2 = int(input())
magic_n = int(input())

count = 0
is_detected = False

for i in range(n1, n2 + 1):
    for n in range(n1, n2 + 1):
        count += 1
        if (i + n) == magic_n:
            print(f'Combination N:{count} ({i} + {n} = {magic_n})')
            is_detected = True
    if is_detected:
        break

if not is_detected:
    print(f'{count} combinations - neither equals {magic_n}')
