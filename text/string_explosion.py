text = input()
strength = 0
now_text = ''
for index in range(len(text)):
    if strength > 0 and text[index] != '>':
        strength -= 1
    elif text[index] == '>':
        strength += int(text[index + 1])
        now_text += text[index]
    else:
        now_text += text[index]
print(now_text)
