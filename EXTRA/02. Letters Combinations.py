first_char = ord(input())
second_char = ord(input())
escape_char = ord(input())

counter = 0

for a in range(first_char, second_char + 1):
    for b in range(first_char, second_char + 1):
        for c in range(first_char, second_char + 1):
            if a != escape_char and b != escape_char and c != escape_char:
                print(f'{chr(a)}{chr(b)}{chr(c)}', end=" ")
                counter += 1

print(counter)
