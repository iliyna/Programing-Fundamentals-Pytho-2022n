ascii_dictionary = {}

list_of_characters = input().split(', ')
for character in list_of_characters:
    ascii_dictionary[character] = ord(character)
print(ascii_dictionary)
# characters = {key: ord(key) for key in list_of_characters} - capriceishan