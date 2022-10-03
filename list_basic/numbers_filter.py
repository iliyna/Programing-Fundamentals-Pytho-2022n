num = int(input())
COMMAND_EVEN = 'even'
COMMAND_ODD = 'odd'
COMMAND_NEGATIVE = 'negative'
COMMAND_POSITIVE = 'positive'
my_lst = []
for i in range(num):
    curr_num = int(input())
    my_lst.append(curr_num)
commands = input()
filtered_my_lst = []
for curr_num in my_lst:
    filtered_passes = (
        (commands == COMMAND_EVEN and curr_num % 2 == 0) or
        (commands == COMMAND_ODD and curr_num % 2 != 0) or
        (commands == COMMAND_POSITIVE and curr_num >= 0) or
        (commands == COMMAND_NEGATIVE and curr_num < 0)
        )
    if filtered_passes:
        filtered_my_lst.append(curr_num)
print(filtered_my_lst)

