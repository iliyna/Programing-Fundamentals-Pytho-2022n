string_cards = input().split()
count_of_faro = int(input())
for count in range(count_of_faro):
    final_string_cards = []
    middle_cards = len(string_cards) // 2
    left_cards = string_cards[0:middle_cards]
    right_cards = string_cards[middle_cards::]
    for index in range(len(left_cards)):
        final_string_cards.append(left_cards[index])
        final_string_cards.append(right_cards[index])
    string_cards = final_string_cards

print(string_cards)
