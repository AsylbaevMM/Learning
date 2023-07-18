

names = ['Иван', "Петр", "Михаил"]
pays = [10000, 15000, 20000]
percents = ['50.25%', "20%", "30.6%"]

result = {name: pay*(float(percent[:-1])/100) for name, pay, percent in zip(names, pays, percents)} 


print(result)   