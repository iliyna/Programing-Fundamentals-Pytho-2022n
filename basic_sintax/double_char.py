string = input()
total = ''
while string != 'End':
    if string == 'End':
        break
    elif string == 'SoftUni':
        string = input()
        continue
    total = ''
    for ch in string:
        total += ch
        total += ch
    print(f'{total}')

    string = input()
