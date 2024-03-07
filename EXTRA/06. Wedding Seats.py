first_sector = ord('A')
last_sector = ord(input())
rows_first_sector = int(input())
seats_odd_rows = int(input())
seats_even_rows = seats_odd_rows + 2
assignments = 0

for sector in range(first_sector, (last_sector + 1)):
    for row in range(1, rows_first_sector + (sector - 64)):
        for seat in range(97, 97 + (seats_even_rows if row % 2 == 0 else seats_odd_rows)):
            print(f'{chr(sector)}{row}{chr(seat)}')
            assignments += 1

print(assignments)
