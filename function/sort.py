number = input().split(' ')

my_lst = number
my_lst_new = []
for digits in my_lst:
    digits_ = int(digits)
    my_lst_new.append(digits_)
my_lst_new.sort()
print(my_lst_new)
