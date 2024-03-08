n = int(input())


for a in range(0, n + 1):
    text = '*' * a
    print(text.rjust(n, ' ') + ' | ' + text.ljust(n, ' '))
