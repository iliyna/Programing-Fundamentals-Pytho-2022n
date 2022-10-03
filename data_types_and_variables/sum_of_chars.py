number_of_lines = int(input())
total_sum = 0
for lines in range(number_of_lines):
    curr_lines = input()
    total_sum += ord(curr_lines)
print(f'The sum equals: {total_sum}')
