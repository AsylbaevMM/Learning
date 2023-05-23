from random import shuffle

# функция для создания правильной кучи. Принимает массив, длину массива, индекс проверяемого элемента 
def makeHeap(arr, size, i):
    #объявляем первый корневой элемент, условно считаем его наибольшим
    largest = i
    left = 2*i + 1
    right = 2*i + 2

    #Проверяем существование дочерних элементов, сравниваем с корневым, 
    # если дочерний больше назначаем его наибольшим
    if left < size and arr[left] > arr[i]:
        largest = left

    if right < size and arr[right] > arr[largest]:
        largest = right

    #Проверяем, изменился ли наибольший элемент, если да, то ставим его в корень и
    # рекурсивно вызываем на него эту же функцию

    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        makeHeap(arr, size, largest)

# Основная функция для сортировки массива
def heapSort(arr):
    size = len(arr)
    # проходимся по всем элементам для приведения дерева к правильному состоянию
    for i in range(size, -1, -1):   # идем с конца массива до 0 элемента с шагом -1
        makeHeap(arr, size, i) 

    # теперь отправляем максимальный элемент в конец массива 
    # и поднимаем вверх следующий по величине
    for i in range(size-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        makeHeap(arr, i, 0)


# проверка работы сортировки
arr = list(range(101)) # создаем массив размером 100 с числами от 0 до 100
shuffle(arr)           # перемешиваем
print('Unsorted array:')  # вывод изначального массива
print(arr)

heapSort(arr)   # сортировка

print("Sorted array:")  # Вывод отсортированного массива 
print(arr)
