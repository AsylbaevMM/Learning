from collections import Counter


friends = {"Саша": ("Палатка", "Тушенка", "Лопата", "Удочка"), 
           "Паша": ("Палатка", "Тушенка", "Удочка"),
           "Дима": ("Палатка", "Удочка", "Топор", "Лопата"),
           "Ваня": ("Палатка", "Лопата", "Огниво")}

have_all = set()
for i in friends.values():
    have_all |= set(i)
print(f"У ребят в арсенале: {have_all}")

uniques = set()
for i in friends:
    temp = set(friends[i])
    for j in friends:
        if j == i:
            continue
        temp -= set(friends[j])
    uniques |= temp
print(f"Уникальные предметы: {uniques}")


things_count = Counter(sum([list(i) for i in friends.values()], start = []))
for i in things_count:
    if things_count[i] == len(friends) - 1:
        for j in friends:
            if i not in friends[j]:
                print(f"{j} забыл {i}")