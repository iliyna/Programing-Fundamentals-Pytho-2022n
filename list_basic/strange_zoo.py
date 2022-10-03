my_lst = []

for curr in range(3):
    curr_text = input()
    my_lst.append(curr_text)
my_lst[0], my_lst[2] = my_lst[2], my_lst[0]
print(my_lst)

