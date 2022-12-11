from calc import calc_main   
from sum_digit import main_sum_digit
from fact_list import main_fact
from only import main_only
import time


def calc():
    print('В этом домашнем задании реализована программа вычисления выражения и улучшены три предыдущие задачи.')
    print('Программа вычисления выражений:')
    print("Парсинг улучшен, можно вводить выражение без пробелов, можно с пробелами, все будет обработано")
    calc_main()
    print()


def other():

    print('''Сумма чисел вещественного числа. Новый код выглядит так:
    print(sum(int(i) for i in filter(lambda x: x.isdigit(), list(input())))) ''')
    main_sum_digit()
    input('Для продолжения нажмите enter')
    print()
    
    print('''Вывод массива факториалов. Новый код выглядит так:
        from math import factorial as f
        print([f(i) for i in range(1, int(input("Введите число >>> "))+1)])  ''')
    main_fact()
    input('Для продолжения нажмите enter')
    print()
  
    print('''Нахождение неповторяющихся элементов массива. Новый код выглядит так:
        from random import randint
        origin_list = [randint(1,15) for i in range(randint(10,15))]
        print(f'Исходный список: {origin_list}')
        print(f'Уникальные значения: {list(filter(lambda x: origin_list.count(x)==1, origin_list))}')''')
    main_only()
    input('Для продолжения нажмите enter')
    print()

choice = input('Введите число: 1 > Калькулятор, 2 > Обновленные решения >>> ')

vars = {'1': calc, '2': other}

vars[choice]()

