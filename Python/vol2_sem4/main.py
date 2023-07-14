

# def to_ord(string):
#     return sorted(set(map(ord, list(string))), reverse = True)


# to_ord = lambda x: sorted(set(map(ord, list(x))), reverse = True)

# print(to_ord('Карл у Клары украл кораллы'))

# print(ord('a'))
# print(chr(99))

# from pprint import pprint

# def grants_dict(names, pays, percents):
#     percents  = list(map(lambda x: float(x[:-1])/100, percents))
#     return {name: pay*percent for name, pay, percent in zip(names, pays, percents) }

# names = ['Иван', "Петр", "Михаил"]
# pays = [10000, 15000, 20000]
# percents = ['50.25%', "20%", "30.6%"]


# pprint(grants_dict(names, pays, percents))   



# def cut_cum(lst, start, stop):
#     return sum(lst[min(start, stop)+1:max(start, stop)])


# lst = [i for i in range(100)]

# print(cut_cum(lst, 95, 105))

# all(True, True, True) = > True
# all(True, False, True) = > False

#any(True, False, Fale) = > True
#any(False, False, Fale) = > False


# def is_all_rentable(companies):
#     return all([sum(i) > 0 for i in companies.values()])

# dict_companies = {}

# company_names = ["aaa", "bbb", "ccc"]
# aaa_digit = [10, -20, 30, 40]
# bbb_digit = [21, 212, -44]
# ccc_digit = [333, -3333, 22222]

# dict_companies[company_names[0]] = aaa_digit 
# dict_companies[company_names[1]] = bbb_digit 
# dict_companies[company_names[2]] = ccc_digit

# print(is_all_rentable(dict_companies))



numbers = [1, 2, 3]
s = 'super'
letter = 'a'

def rename():
    variables = globals()
    temp = {}
    for key, value in variables.items():
        if len(key) > 1 and key.endswith('s'):
            temp[key[:-1]] = variables[key]
            temp[key] = None
    variables.update(temp)
        
rename()


print({key: values for key, values in locals().items() if not key.startswith('__')})