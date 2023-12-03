import openpyxl
import json
 
wb = openpyxl.load_workbook('Role.xlsx')

sheet = wb.active

perms = {}


for i in sheet:
    if i[2].value not in perms:
        perms[i[2].value] = []
    perms[i[2].value].append(i[3].value.split(' DMO ')[-1])

with open('rolesforperms.json', 'w', encoding='utf-8') as file:
    json.dump(perms, file, indent=2)


roles = {}


for i in sheet:
    if i[3].value.split(' DMO ')[-1] not in roles:
        roles[i[3].value.split(' DMO ')[-1]] = []
    roles[i[3].value.split(' DMO ')[-1]].append(i[2].value)

with open('permsforroles.json', 'w', encoding='UTF-8') as file:
    json.dump(roles, file, indent=2)