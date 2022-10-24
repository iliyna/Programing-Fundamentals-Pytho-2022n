numbers = input().split(' ')
numbers_ = numbers

numbers_lst = []

for digits in numbers_:
    digits_ = int(digits)
    numbers_lst.append(digits_)
min_num = min(numbers_lst)
max_num = max(numbers_lst)
sum_digits = sum(numbers_lst)

print(f'The minimum number is {min_num}')
print(f'The maximum number is {max_num}')
print(f'The sum number is: {sum_digits}')
