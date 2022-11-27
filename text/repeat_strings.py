sequence_of_strings = input().split()
lst = []
for strings in sequence_of_strings:
    now_strings = strings * len(strings)
    lst.append(now_strings)
print(''.join(lst), end='')
