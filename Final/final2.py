
array = [input() for i in range(int(input('Введите количество элементов массива >>> ')))]
print(f'Ваш массив: {array} ')
result_array = [i for i in array if len(str(i)) <= 3]
print(f'Обработанный массив: {result_array}')