def factorial_division(number):
    for curr_num in range(1, number):
        number *= curr_num
    return number


first_numbers = int(input())
second_number = int(input())
first_numbers_factorial = factorial_division(first_numbers)
second_number_factorial = factorial_division(second_number)
final_result = first_numbers_factorial / second_number_factorial
print(f'{final_result:.2f}')
