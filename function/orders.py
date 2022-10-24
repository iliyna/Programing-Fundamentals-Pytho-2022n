def order(products, quantity):
    if products == 'coffee':
        return quantity * 1.50
    elif products == 'water':
        return quantity * 1.00
    elif products == 'coke':
        return quantity * 1.40
    elif products == 'snacks':
        return quantity * 2.00


products_name = input()
quantity_the_products = int(input())
result = order(products_name, quantity_the_products)
print(f'{result:.2f}')
