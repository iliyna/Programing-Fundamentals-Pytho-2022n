numbers = list(map(float, input().split()))
my_lst = []
for num in numbers:
    curr_num = round(num)
    my_lst.append(curr_num)
print(my_lst)
