def status( num):
    if num == 100:
        return '100% Complete!\n[%%%%%%%%%%]'
    return f'{num}% [{"%" * (num // 10)}{"." * (10 - num // 10)}]\n Still loading...'


number = int(input())
print(status(number))
