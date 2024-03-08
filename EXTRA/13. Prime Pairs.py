
start_a = int(input())
start_b = int(input())
end_a = start_a + int(input())
end_b = start_b + int(input())


def is_prime(_a, _b):
    flag = True
    for i in range(2, _a // 2 + 1):
        if _a % i == 0:
            flag = False
    for i in range(2, _b // 2 + 1):
        if _b % i == 0:
            flag = False
    return flag


for a in range(start_a, end_a + 1):
    for b in range(start_b, end_b + 1):
        if is_prime(a, b):
            print(f'{a}{b}')
