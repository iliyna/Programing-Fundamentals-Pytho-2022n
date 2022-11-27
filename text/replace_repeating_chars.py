string = input()
now_string = ''
last_character = ''
for ch in string:
    if last_character == ch:
        continue
    else:
        now_string += ch
    last_character = ch
print(now_string)
