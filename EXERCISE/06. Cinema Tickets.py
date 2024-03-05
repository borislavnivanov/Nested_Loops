student = 0
standard = 0
kid = 0
flag_break = False

while True:
    name = input()
    seats = int(input())
    full = 0

    while True:
        inp = input()

        if inp == 'Finish' or inp == 'End':
            print(f'{name} - {(full / seats) * 100:.2f}% full.')
            if inp == 'Finish':
                flag_break = True
            break
        full += 1
        if inp == 'student':
            student += 1
        elif inp == 'standard':
            standard += 1
        elif inp == 'kid':
            kid += 1

    if flag_break:
        break

total_tickets = student + standard + kid

print(f"Total tickets: {total_tickets}")
print(f"{(student / total_tickets) * 100:.2f}% student tickets.")
print(f"{(standard / total_tickets) * 100:.2f}% standard tickets.")
print(f"{(kid / total_tickets) * 100:.2f}% kids tickets.")
