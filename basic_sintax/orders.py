number_of_orders = int(input())

price = 0
total_price = 0

for orders in range(1, number_of_orders + 1, 1):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())
    if price_per_capsule < 0.01 or price_per_capsule > 100:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsules_needed_per_day < 1 or capsules_needed_per_day > 2000:
        continue
    price = days * capsules_needed_per_day * price_per_capsule
    total_price += price
    print(f'The price for the coffee is: ${price:.2f}')
print(f'Total: ${total_price:.2f}')
