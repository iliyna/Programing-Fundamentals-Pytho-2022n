def palindrome(digits):
    if digits == digits[::-1]:
        print('True')
    else:
        print('False')


number = input().split(', ')
number_lst = number
len_number_lst = len(number_lst)
for digit in number_lst:
    palindrome(digit)
