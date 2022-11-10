array = [123, 'example', 22.333 ,['GeekBrains', 'is', 'best'],  12345, 'tea', '777' , 1.2 ]
result_array = []
for i in array:
    if type(i) is int or type(i) is float:         #создаем проверку для обработки данных типа int и float
        if len(str(i)) <= 3:
            result_array.append(i)
    else:
        if len(i) <=3:   
            result_array.append(i)
print(result_array)