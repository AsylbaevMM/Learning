from itertools import combinations
from pprint import pprint


things = {"Тушенка": 1, 
          "Топор": 2, 
          "Спальник": 2, 
          "Палатка": 2, 
          "Выпивка": 12, 
          "Лопата": 3,
          "Котелок": 3,
          "Столовые приборы": 1,
          "Дождевик": 2,
          "Тренога": 1,
          "Крупы": 3,
          "Макароны": 2,
          "Аптечка": 1,
          }

print("Вот вещи, которые можно взять и их массы:")
pprint(things)
storage = int(input('Введите грузоподъемность рюкзака >>> '))
min_storage = int(input('А сколько минимум можем нести? >>> '))

variables = []
for i in range(len(things)):
    variables.extend(list(combinations(things, i+1)))

result = list(filter(lambda x: min_storage <= sum([things[i] for i in x]) <= storage, variables))

print(f"\nВ рюкзак вместительностью {storage} мы можем взять следующие вещи:\n")
for i in sorted(result, key = lambda x: sum([things[i] for i in x]), reverse = True):
    print(f"{', '.join(i)} - суммарная масса: {sum([things[j] for j in i])}")
