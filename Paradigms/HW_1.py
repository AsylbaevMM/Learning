from random import randint


def random_list(lst_size):
    lst = []
    for i in range(lst_size):
        lst.append(randint(1, 99))
    return lst


def sort_list_imperative(numbers):
    for i in range(len(numbers)-1):
        for j in range(len(numbers)-i-1):
            if numbers[j] < numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers


def sort_list_declarative(numbers):
    return sorted(numbers, reverse=True)


size = 10
initial_list = random_list(size)
print(f'initial_list: \t\t{initial_list}')
print(f'Imperative sort: \t{sort_list_imperative(initial_list)}')

print('=============================')

initial_list = random_list(size)
print(f'initial_list: \t\t{initial_list}')
print(f'Declarative sort: \t{sort_list_declarative(initial_list)}')