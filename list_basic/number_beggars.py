single_string_of_integers = input().split(', ')

my_lst = []

for string in single_string_of_integers:
    my_lst.append(int(string))
count_of_beggars = int(input())
final_many = []
index = 0
while index < count_of_beggars:
    sum_for_cur_beggars = 0
    for curr_index in range(index, len(my_lst), count_of_beggars):
        sum_for_cur_beggars += my_lst[curr_index]
    final_many.append(sum_for_cur_beggars)
    index += 1
print(final_many)
