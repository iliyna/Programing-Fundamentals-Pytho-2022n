bakery = {}

key_value = input()
while key_value != 'statistics':

    key, value = key_value.split(': ')
    if key not in bakery.keys():
        bakery[key] = 0
    bakery[key] += int(value)
    key_value = input()
print(f'Products in stock:')
for key, value in bakery.items():
    print(f'- {key}: {value}')
print(f'Total Products: {len(bakery.keys())}')
print(f'Total Quantity: {sum(bakery.values())}')
