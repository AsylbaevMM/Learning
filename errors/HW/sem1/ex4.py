def div_arrays(arr1, arr2):
    if len(arr1) != len(arr2):
        return 'lenerror'
    if 0 in arr2:
        result = []
        for i in range(len(arr2)):
            if arr2[i] == 0:
                result.append(i)
        return ', '.join([str(i) for i in result])
    return list(map(lambda x: x[0]/x[1], zip(arr1, arr2)))


def check_arrays(arr1, arr2):
    result = div_arrays(arr1, arr2)
    if isinstance(result, str):
        if result == 'lenerror':
            print('Длины массивов разные')
        else:
            print(f'Во втором массиве есть элементы равные 0 на позициях: {result}')
    else:
        print(*result)

def main():
    arr1 = [i for i in range(5)]
    arr2 = [i for i in range(2, 7)]
    print('Первый вызов:')
    check_arrays(arr1, arr2)

    arr3 = [i for i in range(5)]
    arr4 = [i for i in range(4)]
    print('\nВторой вызов:')
    check_arrays(arr3, arr4)

    arr1 = [i for i in range(5)]
    arr2 = [1, 0, 3, 0, 5]
    print('\nТретий вызов:')
    check_arrays(arr1, arr2)    


main()