
array = input('Введите элементы массива через пробел >>> ').split()
print(f'Ваш массив: {array} ')
result_array = [i for i in array if len(i) <= 3]
print(f'Обработанный массив: {result_array}')