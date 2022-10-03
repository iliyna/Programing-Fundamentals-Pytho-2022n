group_size = int(input())
days = int(input())

total_companion = group_size
total_coins = 0

for day in range(1, days + 1):
    total_coins += 50
    total_coins -= total_companion * 2
    if day % 10 == 0:
        total_companion -= 2
    if day % 15 == 0:
        total_companion += 5
    if day % 3 == 0:
        total_coins -= total_companion * 3
    if day % 5 == 0:
        total_coins += total_companion * 20
        if day % 3 == 0:
            total_coins -= total_companion * 2
total_coins_companion = int(total_coins // total_companion)
print(f'{total_companion} companions received {total_coins_companion} coins each.')
