def number_odd_even(number):
    sum_of_odd_digits = 0
    sum_of_even_digits = 0
    for digits in number:
        if int(digits) % 2 == 0:
            sum_of_even_digits += int(digits)
        else:
            sum_of_odd_digits += int(digits)
    return sum_of_odd_digits, sum_of_even_digits


number_string = input()
sum_of_odd_digits, sum_of_even_digits = number_odd_even(number_string)
print(f'Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}')
