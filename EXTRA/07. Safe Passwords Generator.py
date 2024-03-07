limiter_a = int(input())
limiter_b = int(input())
max_generated = int(input())

flag = False
counter = 0

for a in range(35, 55):
    for b in range(64, 96):
        for c in range(1, limiter_a + 1):
            for d in range(1, limiter_b + 1):

                print(f'{chr(a)}{chr(b)}{c}{d}{chr(b)}{chr(a)}', end='|')

                a += 1
                if a > 55:
                    a = 35
                b += 1
                if b > 96:
                    b = 64

                counter += 1
                if counter == max_generated:
                    flag = True
                    break
                if c == limiter_a and d == limiter_b:
                    flag = True
                    break
            if flag:
                break
        if flag:
            break
    if flag:
        break
