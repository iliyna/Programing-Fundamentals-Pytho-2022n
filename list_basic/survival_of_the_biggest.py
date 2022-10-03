list_of_integer = input().split()
count_of_numbers_to_remove = int(input())
my_lst = []
for num in list_of_integer:
    my_lst.append(int(num))

for _ in range(count_of_numbers_to_remove):
    my_lst.remove(min(my_lst))

print(', '.join(map(str, my_lst)))
