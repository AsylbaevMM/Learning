# nums = '345  5 456 6765 3 5 67578 34 '
# nums = [int(i) for i in nums.split()]
# print(max(nums), min(nums))



#Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами


# string = '-5x^2 - 7x + 3 = 0'


# a, lit1, b, lit2, c = string[:-3].split()
# b = lit1 + b  
# c = lit2 + c
# a = int(a[:a.index('x')])
# b = int(b[:b.index('x')])
# c = int(c)
# D = b*b - 4 * a * c
# if D < 0:
#     print('Корней нет')
# elif D == 0:
#     print(f'x = {-b/(2*a)}')     
# else:
#     print(f"x1 = {round((-b + D**0.5)/(2*a), 2)}, x2 = {round((-b - D**0.5)/(2*a),2)}")

# from math import gcd
# from random import randrange
# a, b = randrange(1, 1000), randrange(1, 1000)
# if a > b:
#     a, b = b, a
# flag = False
# print(a, b)
# for i in range(2, b+1):
#     if a % i == 0 and b % i == 0:
#         print(f'НОК = {i}')
#         flag = True
#         break

# if not flag:
#     print("НОК не существует")


# from random import randrange
# a, b = randrange(1, 100), randrange(1, 100)
# if a > b:
#     a, b = b, a
# i = b
# print(a, b)
# while True:
#     if i % a == 0 and i % b == 0:
#         print(f'НОК = {i}')
#         break
#     i += 1


# Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
import  math
def find_mult(num):
    multipliers = []
    div = 2
    while num > 1:
        while num % div == 0:
            multipliers.append(div)
            num //= div
        div += 1
    return  multipliers

a, b = 18, 48
multipliers_a = find_mult(a)
multipliers_b= find_mult(b)


print(multipliers_a,multipliers_b)
res=1
for i in set(multipliers_b).intersection(set(multipliers_a)):
    res*=i
print('Наибольший общий делитель:',res)
print(round(a*b/res))
