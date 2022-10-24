def ascii_code(first, second):
    my_lst = []
    for num in range(first + 1, second):
        my_lst.append(num)
    return my_lst


first_characters = input()
second_characters = input()
ascii_code(ord(first_characters), ord(second_characters))

print(' '.join(map(chr, ascii_code(ord(first_characters), ord(second_characters)))))
