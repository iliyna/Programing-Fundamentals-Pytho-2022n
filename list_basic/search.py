num = int(input())
name = input()
my_lst = []
for _ in range(num):
    strings = input()
    my_lst.append(strings)
print(my_lst)
for i in range(len(my_lst) - 1, -1, -1):
    element = my_lst[i]
    if name not in element:
        my_lst.remove(element)
print(my_lst)
