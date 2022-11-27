import re
phone_number = input()
valid_phone_number = r'\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b'
matches = re.findall(valid_phone_number, phone_number)
print(', '.join(matches))
