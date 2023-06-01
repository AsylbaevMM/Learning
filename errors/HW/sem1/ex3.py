def sum_arrays(array1, array2):
    if len(array1) == len(array2):
        return list(map(sum, zip(array1, array2)))
    return 'Lenght error'

def try_sum(array1, array2):
    result = sum_arrays(array1, array2)
    if result == 'Lenght error':
        print('Длины массивов разные')
    
    else:
        print(*result, sep = ' ')

def main():
    arr1 = [i for i in range(5)]
    arr2 = [i for i in range(2, 7)]
    print('Первый вызов:')
    try_sum(arr1, arr2)

    arr3 = [i for i in range(5)]
    arr4 = [i for i in range(4)]
    print('\nВторой вызов:')
    try_sum(arr3, arr4)

main()