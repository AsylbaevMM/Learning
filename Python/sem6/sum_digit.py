
# За основу берем первую задачу второго семинара:  Сумма всех чисел вещественного числа

# Старый код:
# def ex1b():    # Вариан решения через string
#     num = input()
#     total = 0
#     for i in num:   # Перебираем строку, ищем цифры
#         if i.isdigit():
#             total += int(i)
#     print(total)

# Новый код:
# Используется lambda, filter, list comprehension

def main_sum_digit():
    print(sum(int(i) for i in filter(lambda x: x.isdigit(), list(input('Введите число >>> ')))))

