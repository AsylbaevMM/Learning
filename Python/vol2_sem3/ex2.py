from random import sample


#создаем список из случайных элементов
numbers = [i for i in range(10)] * 3
sample_list = sample(numbers, 15)
print("Исходный список:", *sample_list)

# за дубликаты принял элементы, количество которых в списке == 2
result = set()
for i in sample_list:
    if sample_list.count(i) == 2:  # Если нужны элементы, которых больше одного, надо заменить == 2 на > 1
        result.add(i)
print("В исходном списке дублируются:", *result)