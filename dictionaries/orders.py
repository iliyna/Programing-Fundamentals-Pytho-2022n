items = {}
names_prices_quantities = input()
while names_prices_quantities != 'buy':
    names = names_prices_quantities.split()[0]
    price = float(names_prices_quantities.split()[1])
    quantity = int(names_prices_quantities.split()[2])
    if names not in items.keys():
        items[names] = []
        items[names].append(price)
        items[names].append(quantity)
        names_prices_quantities = input()
    else:
        if items[names][0] != price:
            items[names][0] = price
        items[names][1] += quantity

        names_prices_quantities = input()

for key, value in items.items():
    total_price = value[0] * value[1]
    print(f"{key} -> {total_price:.2f}")
