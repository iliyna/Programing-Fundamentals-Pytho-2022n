number_of_rooms = int(input())

total_chairs = 0
total_visitors = 0
needed_chairs = 0
for rooms in range(1, number_of_rooms + 1, 1):
    chairs_number_of_visitors = input().split()
    chairs = len(chairs_number_of_visitors[0])
    visitors = int(chairs_number_of_visitors[1])
    total_chairs += chairs
    total_visitors += visitors
    if chairs < visitors:
        needed_chairs += visitors - chairs
        print(f'{visitors - chairs} more chairs needed in room {rooms}')

if needed_chairs == 0:
    print(f'Game On, {total_chairs - total_visitors} free chairs left')

