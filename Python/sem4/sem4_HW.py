def ex1():                  
    from math import pi             
    d = input('Введите d >>> ')             
    str_pi = str(pi)                    # Превращаем число ПИ в строку
    print(str_pi[:len(d)])              # Берем срез от ПИ по размеру d


def ex3a():   # решение через голичество вхождений
    from random import randrange
    nums = [randrange(0, 100) for i in range(randrange(10, 20))]
    result = []
    for i in nums:                      # Проходимся по списку значений
        if nums.count(i) == 1:          # Добавляем значение в результирующий список, если его количество  == 1
            result.append(i)
    print(f'Исходный список чисел: {sorted(nums)}')
    print(f'Неповторяющиеся значения: {sorted(result)}')      

def ex3b():  # решение через подсчет количества при помощи словаря
    from random import randrange
    nums = [randrange(0, 100) for i in range(randrange(10, 20))]
    result = {}           # Создаем пустой словарь
    alone_nums = []       # Создаем пустой результирующий список
    for i in nums:        # проходимся по исходному списку
        if i in result:   # Если элемент есть в словаре, увеличиваем его количество на 1
            result[i] += 1   
        else:             # Если отсутсвует, элемент со значением = 1
            result[i] = 1
    for i in result:      # проходимся по словарю
        if result[i] == 1:     # Если количество = одному заносим этот элемент в результирующий список
            alone_nums.append(i)
    print(f'Исходный список чисел: {sorted(nums)}')
    print(f'Неповторяющиеся значения: {sorted(alone_nums)}')  



def ex4():
    from random import randrange, choice
    with open('file.txt', 'w' ) as output_file:
        k = int(input('Введите степень k >>> '))    # Получаем необходимую степень
        result = []                                 # Создаем пустой словарь для накопления случайными членами
        for i in range(k, 1, -1):                   # Создаем цикл на к итераций
            C = randrange(0, 101)                   # Создаем коэффициенты 
            if C > 1:                               # В зависимости от коэффициента создаем член многочлена и добавляем в список
                result.append(f'{C}*x^{i}')
            elif C == 1:
                result.append(f'x^{i}')
            else:
                continue
        result_str = f'{result[0]}'                 # Создаем результирующий список и сразу вносим в него первый элемент
        for i in range(1, len(result)):             # Продолжаем наполнять список
            result_str += choice([' - ', ' + ']) + result[i]     # Ставим случайный знак перед каждым членом
        result_str += f"{choice([' - ', ' + '])}{randrange(0, 101)}*x + {randrange(0, 101)} = 0"   # Добавляем последнюю переменную и = 0
        print(result_str, file = output_file)


def ex5():
    def destr(arg, sign = '+'):           # Функиця , которая принимает член вида C*x^n и возвращает список из степени и переменной
        if 'x' in arg:
            C = int(sign + arg[:arg.index('*')])
            if '^' in arg:
                n = int(arg[arg.index('^')+1:])
            else:
                n = 1
        else:
            C = int(arg)
            n = 0
        return [n, C]

    def parce(file):                    # Функция, которая принмает файл и возвращает словарь, где ключи = степеням, а значения = коэффициентам
        string = file.readline().rstrip()[:-3]
        a, *args = string.split()
        new_args = {destr(a)[0]: destr(a)[1]}
        for i in range(1, len(args), 2):
            new_args[destr(args[i], args[i-1])[0]]  =  destr(args[i], args[i-1])[1]
        return new_args

    with open('input1.txt', 'r') as input1, open('input2.txt', 'r') as input2, open('file.txt', 'w') as output_file:
        result = parce(input1)  # Тут используя 2 вышестоящие функции получаем два словаря на основе входных документов
        data2 = parce(input2) 
        for i in data2:         # Проходимся по второму словарю и пополняем первый(который решили сделать результирующим)
            if i in result:
                result[i] += data2[i]
            else:
                result[i] = data2[i]        
        result_string = f'{result[max(result)]}*x^{max(result)}' #Создаем начало строки используя элемент словаря с макисмальным ключом(который равен степени)
        del result[max(result)]         # Удаляем этот элемент, дабы не мешал
        for i in sorted(result, reverse = True):
            if result[i] > 0:                      # продолжаем наполнять строку учитывая значения коэффициентов и степеней
                result_string += ' + ' + str(result[i])
            elif result[i] < 0:
                result_string += ' - ' + str(result[i])[1:]
            else:
                continue
            if i > 1:
                result_string += '*x^' + str(i)
            elif i == 1:
                result_string += '*x'
        result_string += ' = 0'      #не забываем добавить  "= 0" в конце
        print(result_string, file = output_file)  
        

ex1()
ex3a()
ex3b()
ex4()
ex5()