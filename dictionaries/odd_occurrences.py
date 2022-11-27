word = input().split(' ')
words = {}
for item in word:
    item_lower = item.lower()
    if item_lower not in words:
        words[item_lower] = 0
    words[item_lower] += 1
for key, value in words.items():
    if value % 2 != 0:
        print(key, end=' ')
