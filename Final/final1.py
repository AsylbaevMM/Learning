array = [123, 'example', 22.333 ,'aloha',  12345, 'tea', '777' , 1.2 ]
result_array = []
for i in array:
    if len(str(i)) <= 3:
            result_array.append(i)
print()
print(f'Исходный массив: {array}')            
print(f'Обработанный массив: {result_array}')
print()