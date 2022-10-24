def positive_filter(numbers):
    return [num for num in numbers if int(num) >= 0]


def negative_filter(numbers):
    return [num for num in numbers if int(num) < 0]


def even_filter(numbers):
    return [num for num in numbers if int(num) % 2 == 0]


def odd_filter(numbers):
    return [num for num in numbers if int(num) % 2 != 0]


number = input().split(', ')
print(f'Positive: {", ".join(positive_filter(number))}')
print(f'Negative: {", ".join(negative_filter(number))}')
print(f'Even: {", ".join(even_filter(number))}')
print(f'Odd: {", ".join(odd_filter(number))}')
