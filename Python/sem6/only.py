
# За основу берем вторую задачу второго семинара:  Сумма всех чисел вещественного числа

# Старый код:
# def ex3a():   # решение через голичество вхождений
#     from random import randrange
#     nums = [randrange(0, 100) for i in range(randrange(10, 20))]
#     result = []
#     for i in nums:                      # Проходимся по списку значений
#         if nums.count(i) == 1:          # Добавляем значение в результирующий список, если его количество  == 1
#             result.append(i)
#     print(f'Исходный список чисел: {sorted(nums)}')
#     print(f'Неповторяющиеся значения: {sorted(result)}')  


# Новое решение:
# Используется lambda, filter, list comprehension

def main_only():
    from random import randint
    origin_list = [randint(1,15) for i in range(randint(10,15))]
    print(f'Исходный список: {origin_list}')
    print(f'Уникальные значения: {list(filter(lambda x: origin_list.count(x)==1, origin_list))}')
