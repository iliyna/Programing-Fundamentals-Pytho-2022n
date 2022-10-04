the_level_of_fire = input().split('#')
amount_of_water = int(input())
print(f'Cells:')
x = the_level_of_fire
x.reverse()

a = (x[- 1]).split()

b = len(x)
type_of_fire = a[0]
ranges = int(a[2])
extinguished_fires = []
total_fire = 0
effort = 0

for i in range(b):

    if amount_of_water <= 0:
        break

    if type_of_fire == 'High':
        if 81 <= ranges <= 125 and amount_of_water >= ranges:
            amount_of_water -= ranges
            total_fire += ranges
            effort += ranges * 0.25
            extinguished_fires.append(ranges)
            print(f' - {ranges}')

    elif type_of_fire == 'Medium':
        if 51 <= ranges <= 80 and amount_of_water >= ranges:
            amount_of_water -= ranges
            total_fire += ranges
            effort += ranges * 0.25
            extinguished_fires.append(ranges)
            print(f' - {ranges}')

    elif type_of_fire == 'Low' and amount_of_water >= ranges:
        if 1 <= ranges <= 50:
            amount_of_water -= ranges
            total_fire += ranges
            effort += ranges * 0.25
            extinguished_fires.append(ranges)
            print(f' - {ranges}')

    x.pop()
    if i == b - 1:
        break
    a = (x[- 1]).split()
    type_of_fire = a[0]
    ranges = int(a[2])


print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')
