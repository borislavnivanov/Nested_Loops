while True:
    destination = input()
    if destination == 'End':
        break
    budget = float(input())
    savings = 0
    while True:
        savings += float(input())
        if savings >= budget:
            print(f'Going to {destination}!')
            break
