def ex1a():   # Вариант решения через float
    num = abs(float(input()))  # abs для исключения ошибок при обработке отрицательных чисел
    while round(num) != num:   # избавляемся от запятой(умножаем на 10, пока дробной части не останется)
        num *= 10
    total = 0      
    while num > 0: # считаем сумму
        total += num % 10
        num //= 10
    print(int(total))

def ex1b():    # Вариан решения через string
    num = input()
    total = 0
    for i in num:   # Перебираем строку, ищем цифры
        if i.isdigit():
            total += int(i)
    print(total)

def ex2():
    n = int(input())
    nums = [1]
    for i in range(1, n):
        nums.append(nums[i-1] * (i+1))
    print(nums)    

def ex3():
    dct = {i: round((1+(1/i))**i, 2) for i in range(1, int(input()) + 1) }
    print(f'Словарь: {dct}')   
    print(f'Сумма значений: {sum(dct.values())}')


def ex4():
    with open('file.txt', 'r', encoding='utf-8') as input_file:   # открываем файл
        n = int(input())                                        
        nums = [int(i) for i in range(-n, n+1)]                 # создаем список значений от -n до n
        positions = [int(i) for i in map(str.strip, input_file.readlines())]      # считываем строки, создаем из них список целых чисел
        total = 1                                                             # создаем переменную накопитель
        for i in positions:                                                   # перебираем список позиций
            if int(i) < len(nums):                                            # проверяем наличие позиций
                total *= nums[i]                                              # при наличии умножаем накопитель
            else:
                print(f'Отсутствует элемент с индексом {i}')                  # при отсутствии выводим сообщение
        print("Произведение искомых аргументов =", total)                     # вывод результата

def ex5(first = 0, last = 100):  
    import time
    ran = int(str(time.time())[-3:])  # Берем последние 3 цифры текущего времени
    while True:                       # Запускаем бесконечный циклы
        if ran < first:               # Пытаемся привести предыдущее число в рамки заданных значений
            ran += (last - first)
        if ran > last:
            ran -= (last - first)
        if first <=  ran <= last:     # при попадании возвращаем число
            return ran
            break        


ex1a()       # Вариант решения через float
ex1b()       # Вариант через строку
ex2()
ex3()
ex4()
print(ex5()) # По умолчанию задан промежуток [0; 100] для изменения вызвать функцию с другими значениями границ (ex5(нач, конечн)).
             # Функция возвращает, а не печатает число 



