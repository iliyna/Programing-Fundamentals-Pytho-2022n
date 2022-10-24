number_of_wagons = int(input())
wagons = [0] * number_of_wagons


while True:
    command = input()

    if command == 'End':
        break

    command_split = command.split(' ')
    carr_command = command_split[0]
    if carr_command == 'add':
        people = int(command_split[1])
        wagons[-1] += people
    elif carr_command == 'insert':
        people = int(command_split[2])
        index = int(command_split[1])
        wagons[index] += people
    elif carr_command == 'leave':
        index = int(command_split[1])
        people = int(command_split[2])
        wagons[index] -= people

print(wagons)
