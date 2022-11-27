company_names_id = {}

command = input()
while command != "End":
    if command == 'End':
        break
    company, id = command.split(' -> ')
    if company not in company_names_id.keys():
        company_names_id[company] = []
    if  id not in company_names_id[company]:
        company_names_id[company].append(id)
    command = input()
for company in company_names_id.keys():
    print(f'{company}')
    for id in company_names_id[company]:
        print(f'-- {"".join(id)}')
