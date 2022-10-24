def sum_numbers(a, b):
    return a + b


def subtract(sum, c):
    return sum - c


def add_and_subtract(a, b, c):
    sum_of_numbers = sum_numbers(first, second)
    result = subtract(sum_of_numbers, third)
    return result


first = int(input())
second = int(input())
third = int(input())
print(add_and_subtract(first, second, third))
