age = int(input())
drink_something = ''
if age <= 14:
    drink_something = 'toddy'
elif age <= 18:
    drink_something = 'coke'
elif age <= 21:
    drink_something = 'beer'
else:
    drink_something = 'whisky'
print(f'drink {drink_something}')
