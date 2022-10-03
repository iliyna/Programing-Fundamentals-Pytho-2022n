from math import ceil
number_of_people = int(input())
capacity = int(input())
courses = ceil(number_of_people / capacity)
if number_of_people % courses != 0:
    capacity += 1
print(f'{courses}')
