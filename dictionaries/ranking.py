contest_passwords = {}
usernames_points = {}

contest_password = input().split(':')
while len(contest_password) > 1:
    contest, password = contest_password[0], contest_password[1]
    if contest not in contest_passwords:
        contest_passwords[contest] = password
    contest_password = input().split(':')

username_points = input().split('=>')
while len(username_points) > 1:
    contests, passwords, username, points = username_points[0], username_points[1],\
                                            username_points[2], username_points[3]
    point = int(points)
    for key, value in contest_passwords.items():
        if key == contests and value == passwords:
            if key not in usernames_points.keys():
                usernames_points[contests] = []
                usernames_points[contests].append(username)
                usernames_points[contests].append(point)
            else:
                if contests in usernames_points.keys():
                    if point > usernames_points[contests][1]:
                        usernames_points[contests][1] = point
                else:
                    usernames_points[contests].append(username)
                    usernames_points[contests].append(point)
    username_points = input().split('=>')
total_point = 0
best = 0
name = ''
for key, value in usernames_points.items():
    if key == key:
        if value[0] == value[0]:
            best += value[1]
            name = value[0]
            if total_point < best:
                total_point = best
print(f'Best candidate is {name} with total {total_point} points.')
print(f'Ranking:')
for key, value in usernames_points.items():    # ne raboti

    if value[0] == value[0]:
        print(f'{value[0]}')
        print(f'# {key} -> {value[1]}')
