divisor = int(input())
boundary = int(input())
for corr_num in range(boundary, divisor + 1, - 1):
    if corr_num % divisor == 0 and corr_num != 0:
        print(f'{corr_num}')
        break
