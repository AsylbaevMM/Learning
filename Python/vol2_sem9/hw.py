import csv
from random import randint
from functools import wraps
import json
from datetime import datetime


FILENAME = 'test.csv' 

def generate_numbers(smallest, largest, count, file):
    '''все просто, создаем матрицу 3 x count с элементами от smallest до largest, записываем в file'''
    nums = []
    for _ in range(count):
        nums.append([randint(smallest, largest) for _ in range(3)])
    with open(file, 'w', encoding='utf-8', newline = '') as file:
        writer = csv.writer(file)
        writer.writerows(nums)

# Вызываем функцию для создания файла с числами
generate_numbers(-100, 100, 100, FILENAME)


def json_saver(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # пытаемся считать данные из файла в словарь, а если его нет, создаем новый
        try:
            with open(f'{func.__name__}.json', 'r') as file:
                result_dict = json.load(file)
        except:
            result_dict = {}
        # Ключом для каждого вызова служит строковое представление передаваемых аргументов 
        with open(f'{func.__name__}.json', 'w') as file:
            result = func(*args, **kwargs)
            result_dict[str(args)] = result
            json.dump(result_dict, file, indent=3, ensure_ascii=False)
        return result
    return wrapper


def from_file(file):
    '''Этот декоратор "съедает" аргументы функции и в цикле подставляет аргументы из файла'''
    def decorator(func):
        result = {}
        with open(file, 'r', encoding='utf-8') as input_file:
            rows = list(csv.reader(input_file))
        def wrapper(*args, **kwargs):
            for nums in rows:
                input_values = tuple((int(i) for i in nums))
                output_values = func(*input_values)
                result[input_values] = output_values
            return result
        return wrapper
    return decorator    
        

@from_file(FILENAME)
@json_saver
def equation_solver(a, b, c):
    # столкнулся с ZeroDivisionError, если а==0, поэтому обыграл этот момент приведением к обычному уравнению
    if a == 0:
        return -c / b
    D = b ** 2 - 4 * a * c
    if D > 0:
        return (-b + D ** (1 / 2)) / (2 * a), (-b - D ** (1 / 2)) / (2 * a)
    elif D == 0:
        return -b / (2 * a)
    else:
        return None

equation_solver(3, 4, 5)