secret_message = input().split()
coding = []
number = ''
letter = []
num = ''
for text in secret_message:

    for ch in text:
        if ch in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            number += ch
        else:
            letter += ch
    letter[0], letter[-1] = letter[-1], letter[0]

    num += chr(int(number)) + ''.join(letter)
    coding.append(num)
    number = ''
    letter = []
    num = ''

print(' '.join(coding))
