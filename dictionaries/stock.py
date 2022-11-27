food_quantities = input().split(' ')
search_products = input().split(' ')
bakery = {}
for index in range(0, len(food_quantities), 2):
    key = food_quantities[index]
    value = int(food_quantities[index + 1])
    bakery[key] = value
for product in search_products:
    if product not in bakery:
        print(f"Sorry, we don't have {product}")
    else:
        print(f"We have {bakery[product]} of {product} left")
