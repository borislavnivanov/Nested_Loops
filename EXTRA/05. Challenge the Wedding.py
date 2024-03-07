men = int(input())
women = int(input())
tables = int(input())

couples_count = 0

for men in range(1, men + 1):
    for women in range(1, women + 1):
        print(f'({men} <-> {women})', end=' ')
        couples_count += 1
        if couples_count >= tables:
            break
    else:
        continue
    break
