n = int(input())
for _ in range(n):
    num = int(input())
    if num % 2 != 0:
        print(f'{num} is odd!')
        break
else:
    print(f'All numbers are even.')
