start_character = int(input())
last_character = int(input())

for curr_char in range(start_character, last_character + 1):
    print(chr(curr_char), end=' ')
