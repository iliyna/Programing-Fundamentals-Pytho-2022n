import re
text = input()
pattern = r'\b_([A-Za-z0-9]+)\b'
names = re.findall(pattern, text)
print(",".join(names))
