numbers = input().split(' ')
num = numbers
result_ = []
for digits in num:
    digits_ = int(digits)
    result_.append(digits_)
result_ = filter(lambda x: x % 2 == 0, result_)

print(list(result_))
