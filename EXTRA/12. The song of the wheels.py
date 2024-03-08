control_number = int(input())

counter = 0
password = 'Password: '

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a < b and c > d and (a * b + c * d) == control_number:
                    print(f'{a}{b}{c}{d}', end=' ')
                    counter += 1
                    if counter == 4:
                        password += str(a) + str(b) + str(c) + str(d)

if password != 'Password: ':
    print(f'\n{password}')
else:
    print(f'\nNo!')
