# В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

# with open('file.txt', 'r') as input_file:
#     nums = [int(i) for i in input_file.read().rstrip().split()]
#     new_nums = [i for i in range(nums[0], nums[-1]+1)]

# with open('output.txt', 'w') as output_file:
#     print(*nums, sep = ' ', file = output_file)
#     print(*new_nums, sep = ' ', file = output_file)
#     print(f'Lost num: {list(set(nums)^set(new_nums))[0]}', file = output_file)



#____________________________________________________

# import random

# lst = [i for i in range(10)]
# lst.pop(random.randint(0, 9))

# search_num = [i for i in range(1, len(lst)) if lst[i] - lst[i - 1] > 1][0]

# with open('num.txt', 'w') as file:
#     file.write(' '.join(list(map(str, lst))))

# with open('num.txt', 'r') as file:
#     lst_new = file.read().split()
#     print(*lst_new)

# lst_new.insert(search_num, search_num)
# print(*lst_new)

# with open('num.txt', 'a') as file:
#     file.write('\n' + ' '.join(list(map(str, lst_new))))


#________________________________________________________________________

# Дан список чисел. Создайте список, в который попадают числа, 
# описываемые возрастающую последовательность. Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 5] или [1, 4, 6, 7] и т.д.

# nums = [1, 5, 2, 3, 4, 6, 1, 7]
# result = [min(nums),]
# for i in nums:
#     if i > result[-1] and i - result[-1]< 3:
#         result.append(i)
# print(result)


#____________________________________________________________________________
