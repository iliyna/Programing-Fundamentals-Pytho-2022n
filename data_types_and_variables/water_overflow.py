number_of_lines = int(input())
water_tank = 255
total_water = 0
for lines in range(number_of_lines):
    curr_lines = int(input())
    if curr_lines > water_tank:
        print(f'Insufficient capacity!')
        continue
    water_tank -= curr_lines
    total_water += curr_lines
print(f'{total_water}')
