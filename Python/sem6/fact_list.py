# За основу берем вторую задачу второго семинара:  Сумма всех чисел вещественного числа

# Старый код:
# def ex2():
#     n = int(input())
#     nums = [1]
#     for i in range(1, n):
#         nums.append(nums[i-1] * (i+1))
#     print(nums)

# Новый:
# Используется list comprehension, math.factorial

def main_fact():
    from math import factorial as f
    print([f(i) for i in range(1, int(input("Введите число >>> "))+1)])
