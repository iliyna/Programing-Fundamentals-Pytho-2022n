import re
lst = []
total = 0
pattern = r'>>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)'
text = input()
while text != 'Purchase':
    match = re.search(pattern, text)
    if match:
        bought_furniture, price, quantity = match.groups()
        lst.append(bought_furniture)
        total += float(price) * int(quantity)
    text = input()
print(f'Bought furniture:')
for furniture in lst:
    print(furniture)
print(f'Total money spend: {total:.2f}')
