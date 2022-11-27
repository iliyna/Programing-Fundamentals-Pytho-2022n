text = input()
total = ''
now_text = ''
digits = ''

for ch in text:
    if not ch.isdigit():
        if len(now_text) > 0 and len(digits) > 0:
            total += now_text * int(digits)
            now_text = ''
            digits = ''
        now_text += ch
    elif ch.isdigit:
        digits += ch
if len(now_text) > 0 and len(digits) > 0:
    total += now_text * int(digits)
    now_text = ''
    digits = ''

unique = set(total.upper())
print(f'Unique symbols used: {len(unique)}')
print(f'{total.upper()}')
