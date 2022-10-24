def password_validations(lent, digit, other):
    if 6 <= lent <= 10 and digit >= 2 and other == 0:
        print(f'Password is valid')
    if lent < 6 or lent > 10:
        print(f'Password must be between 6 and 10 characters')
    if other > 0:
        print(f'Password must consist only of letters and digits')
    if digit < 2:
        print(f'Password must have at least 2 digits')


password = input()
len_password = len(password)
x_ = (','.join(password))
x = x_.split(',')
digits = 0
letters = 0
others = 0

for i in x:
    a = ord(i)
    if 49 <= a <= 57:
        digits += 1
    elif 65 <= a <= 90:
        letters += 1
    elif 97 <= a <= 122:
        letters += 1
    else:
        others += 1
password_validations(len_password, digits, others)
