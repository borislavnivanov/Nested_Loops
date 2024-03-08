days = int(input())
hours = int(input())

day_sum = 0.00
total_sum = 0.00

for day in range(1, days + 1):
    for hour in range(1, hours + 1):

        if day % 2 == 0 and hour % 2 != 0:
            day_sum += 2.50
        elif day % 2 != 0 and hour % 2 == 0:
            day_sum += 1.25
        else:
            day_sum += 1

    print(f'Day: {day} - {day_sum:.2f} leva')
    total_sum += day_sum
    day_sum = 0.00

print(f'Total: {total_sum:.2f} leva')
