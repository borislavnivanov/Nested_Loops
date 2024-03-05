judges = int(input())
total_score = 0
tasks = 0

while True:
    task = input()
    if task == 'Finish':
        break
    score = 0.00
    for _ in range(judges):
        score += float(input())

    score /= judges
    total_score += score
    print(f'{task} - {score:.2f}.')
    tasks += 1

print(f'Student\'s final assessment is {total_score / tasks:.2f}.')
