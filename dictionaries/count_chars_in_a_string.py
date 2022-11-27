counts = input().split()
symbols = ''.join(counts)
counts_all_characters = {}
for char in symbols:
    if char not in counts_all_characters.keys():
        counts_all_characters[char] = 0
    counts_all_characters[char] += 1
for char, value in counts_all_characters.items():
    print(f'{char} -> {value}')
