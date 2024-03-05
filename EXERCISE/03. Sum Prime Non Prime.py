sum_prime = 0
sum_non_prime = 0

while True:
    client_inp = input()
    if client_inp == 'stop':
        break

    number = int(client_inp)

    if number == 1:
        sum_non_prime += number
    elif number == 0:
        sum_prime += number
    elif number < 0:
        print('Number is negative.')
    else:
        is_prime = True
        for i in range(2, int(number)):
            if number % i == 0:
                is_prime = False

        if is_prime:
            sum_prime += number
        else:
            sum_non_prime += number

print(f'Sum of all prime numbers is: {sum_prime}')
print(f'Sum of all non prime numbers is: {sum_non_prime}')
