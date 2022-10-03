n = int(input())
for x in range(97, (97 + n)):
    for y in range(97, (97 + n)):
        for j in range(97, (97 + n)):
            total = chr(x) + chr(y) + chr(j)
            print(total)
