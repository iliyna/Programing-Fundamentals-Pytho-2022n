numbers_of_string = int(input())

for string in range(1, numbers_of_string + 1, 1):
    curr_string = input()

    if ',' in curr_string or '.' in curr_string or '_' in curr_string:
        print(f"{curr_string} is not pure!")
    else:
        print(f"{curr_string} is pure.")
