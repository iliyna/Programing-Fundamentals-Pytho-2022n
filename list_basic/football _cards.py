teams_a = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
teams_b = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']
red_card = input().split()
terminated = False
for card in red_card:
    if card in teams_a:
        teams_a.remove(card)
    elif card in teams_b:
        teams_b.remove(card)
    if len(teams_a) < 7 or len(teams_b) < 7:
        terminated = True
        break
print(f'Team A - {len(teams_a)}; Team B - {len(teams_b)}')
if terminated:
    print(f'Game was terminated')
