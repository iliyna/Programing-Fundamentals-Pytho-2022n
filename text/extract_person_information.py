number_of_text = int(input())
name = []
age = []

for text in range(number_of_text):
    texts = input().split()
    for word in texts:
        if '@' in word and '|' in word:
            word = word.replace('@', ', ')
            word = word.replace('|', ', ')
            name = word.split()
        if '#' in word and '*' in word:
            word = word.replace('#', ', ')
            word = word.replace('*', ', ')
            age = word.split()
    names = name[1].split(',')
    ages = age[1].split(',')
    print(f'{"".join(names)} is {"".join(ages)} years old.')