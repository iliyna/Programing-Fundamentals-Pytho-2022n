number_of_electrons = int(input())
fill_shells_until = []
index = 0
while number_of_electrons >= 0:
    index += 1
    max_shells = 2 * (index * index)
    if max_shells > number_of_electrons:
        if number_of_electrons > 0:
            fill_shells_until.append(number_of_electrons)
        number_of_electrons = 0
        break
    fill_shells_until.append(max_shells)
    number_of_electrons -= max_shells

print(fill_shells_until)
