budget = int(input())

curr_num = budget
num = input()
while num != 'End':
    number = int(num)
    if number > curr_num:
        print(f'You went in overdraft!')
        break
    curr_num -= number

    num = input()
else:
    print(f'You bought everything needed.')
