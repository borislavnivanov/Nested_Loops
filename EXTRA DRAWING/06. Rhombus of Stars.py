n = int(input())

for i in range(1, n + 1):
    text = '* ' * i
    print(text.center(n * 2, ' '))

for i in range(n - 1, 0, -1):
    text = '* ' * i
    print(text.center(n * 2, ' '))
