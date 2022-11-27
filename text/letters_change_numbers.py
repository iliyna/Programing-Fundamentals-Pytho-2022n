text = input().split()
total_sum = 0

for word in text:
    if word[0].isupper():  # делене
        ch = ord(word[0]) - 64
        num = int(word[1:-1])
        total_sum += num / ch
    elif word[0].islower():  # умножение
        ch = ord(word[0]) - 96
        num = int(word[1:-1])
        total_sum += num * ch
    if word[-1].isupper():  # изваждане
        ch = ord(word[-1]) - 64
        total_sum -= ch
    elif word[-1].islower():  # събиране
        ch = ord(word[-1]) - 96
        total_sum += ch
print(f'{total_sum:.2f}')
