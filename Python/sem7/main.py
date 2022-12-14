
from calc_fraction import calc_fraction_main
from calc_complex import calc_complex_main
from log import log_main
import os



def variable_input():
    a = input("Введите первое число >>> ")
    b = input("Введите второе число >>> ")
    move = input("Введите действие >>> ")
    while move not in ['+', '-', '*', '/']:
        print('Вы ввели некорректное действие')
        move = input("Введите корректное действие >>> ")
    return a, b, move


def final(string):
    print(string)
    log_main(string)

def result_string(func, a, b, move):
    return f'{a} {move} {b} = {func(a, b, move)}'


def main():
    choice = input("Выберите тип чисел: 1.Комплексные, 2.Рациональные >>> ")

    while choice not in '12':
        print('Вы ввели некорректное значение')
        choice = input("Выберите тип чисел: 1.Комплексные, 2.Рациональные >>> ")

    if choice == '1':
        print("Вы выбрали комплексные числа. Введите числа в формате 'a + bj' >>> ")
        result = result_string(calc_complex_main, *variable_input())
        final(result)

    if choice == '2':
        print("Вы выбрали рациональные числа. Введите числа в формате 'a/b' >>> ")
        result = result_string(calc_fraction_main, *variable_input())
        final(result)

   

    again = input('Для нового подсчета введите 1, для выхода нажмите Enter >>> ')
    
    if again == '1':
        main()

main()

    


