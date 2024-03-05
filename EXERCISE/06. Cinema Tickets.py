student = 0
standard = 0
kid = 0

while True:
    name = input()
    seats = int(input())
    flag_break = False
    full = 0

    while True:
        var = input()

        if var == 'Finish' or var == 'End':
            print(f'{name} - {(full / seats) * 100:.2f}% full.')
            if var == 'Finish':
                flag_break = True
            break
        elif var == 'student':
            full += 1
            student += 1
        elif var == 'standard':
            full += 1
            standard += 1
        elif var == 'kid':
            full += 1
            kid += 1

    if flag_break:
        break

total_tickets = student + standard + kid

print(f"Total tickets: {total_tickets}")
print(f"{(student / total_tickets) * 100:.2f}% student tickets.")
print(f"{(standard / total_tickets) * 100:.2f}% standard tickets.")
print(f"{(kid / total_tickets) * 100:.2f}% kids tickets.")
