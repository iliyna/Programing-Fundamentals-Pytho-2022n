num = int(input())
negative = []
positive = []
for _ in range(num):
    curr_num = int(input())
    if curr_num >= 0:
        positive.append(curr_num)
    else:
        negative.append(curr_num)
print(positive)
print(negative)
print(f'Count of positives: {len(positive)}')
print(f'Sum of negatives: {sum(negative)}')
