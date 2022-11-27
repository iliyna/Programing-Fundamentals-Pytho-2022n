collect_the_resources = {}
while True:
    resource = input()
    if resource == 'stop':
        break
    quantity = int(input())
    if resource not in collect_the_resources.keys():
        collect_the_resources[resource] = 0
    collect_the_resources[resource] += quantity

for resource, quantity in collect_the_resources.items():
    print(f"{resource} -> {quantity}")
