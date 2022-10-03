receive_the_gifts = input().split()

gifts = []
for curr_gifts in receive_the_gifts:
    gifts.append(curr_gifts)
comma = input()
while comma != 'No Money':
    if comma == 'No Money':
        break
    command = comma.split()
    comm = command[0]
    gift = command[1]
    if comm == 'OutOfStock':
        if gift in gifts:
            lend = len(gifts)
            br = gifts.count(gift)
            for _ in range(br):
                rez = gifts.index(gift, 0, lend)
                gifts[rez] = 'None'

    elif comm == 'Required':
        index = int(command[2])
        if 0 <= index <= len(gifts):
            gifts[index] = gift
    elif comm == 'JustInCase':
        gifts[-1] = gift
    comma = input()
if 'None' in gifts:
    rem = gifts.count('None')
    for _ in range(rem):
        gifts.remove('None')
print(' '.join(gifts))
