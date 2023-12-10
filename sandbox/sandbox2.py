from pprint import pprint

import openpyxl

wb = openpyxl.load_workbook('roles.xlsx')

sheet = wb.active

result = {}

for row in sheet:
    if row[4].value != 'no':
        result[row[2].value] = row[5].value

pprint(result)