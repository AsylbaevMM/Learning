# Напишите метод, на вход которого подаётся двумерный строковый массив размером 4х4. 
# При подаче массива другого размера необходимо бросить исключение MyArraySizeException.

# Далее метод должен пройтись по всем элементам массива, преобразовать в int и просуммировать. 
# Если в каком-то элементе массива преобразование не удалось (например, в ячейке лежит символ или текст вместо числа), 
# должно быть брошено исключение MyArrayDataException с детализацией, в какой именно ячейке лежат неверные данные.

# В методе main() вызвать полученный метод, обработать возможные исключения MyArraySizeException и MyArrayDataException 
# и вывести результат расчета (сумму элементов, при условии что подали на вход корректный массив).


class MyArraySizeException(Exception):
    pass

class MyArrayDataException(Exception):
    pass

def check_array_size(arr):
    if len(arr) !=4 or any(map(lambda x: len(x) !=4 , arr)):
        raise MyArraySizeException('Размер массива не соответствует 4х4')
    return True
    
def sum_array(arr):
    check_array_size(arr)
    total = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            try:
                total += int(arr[i][j])
            except:
                raise MyArrayDataException(f'В ячейке {i}, {j} неверный формат: {arr[i][j]}')
    return total


   
arr = [[5]*4 for i in range(4)]

#arr[3][2] = 'asd'

print(sum_array(arr))



