numbers_of_messages = int(input())
message = ''
for num in range(numbers_of_messages):
    numbers = int(input())
    if numbers == 86:
        message = 'How are you?'
    elif numbers == 88:
        message = 'Hello'
    elif numbers < 88:
        message = 'GREAT!'
    elif numbers > 88:
        message = 'Bye.'
    print(f'{message}')
