n1 = int(input())
n2 = int(input())

for i in range(n1, n2 + 1):
    sum_equal = 0
    sum_odd = 0
    check = []

    for char in str(i):
        check.append(char)

    for b in range(len(check)):
        if (b + 1) % 2 == 0:
            sum_equal += int(check[b])
        else:
            sum_odd += int(check[b])

    if sum_equal == sum_odd:
        print(f'{i}', end=' ')
