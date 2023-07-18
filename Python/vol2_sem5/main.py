
# a, b, c, *d = input().split('/')
# print(result := {b: a, c:d})
#############################################


# obj = {x: ord(x) for x in input('Введите строку >>> ')}
# iter_obj = iter(obj.items())

# for i in range(5):
#     print(next(iter_obj))

# print(*iter_obj)

############################################

# print(*(i for i in range(0, 101, 2) if sum(map(int, str(i))) != 8))

###########################################

#print(*('FizzBuzz' if not i % 15 else "Buzz" if not i % 5 else "Fizz" if not i % 3 else i for i in range(1, 101)))

###########################################

# for i in range(2, 11):
#     for j in range(2, 6):
#         print(f'{j} X {i} = {i * j}\t', end='\t\t')
#     print()
# print()
# for i in range(2, 11):
#     for j in range(6, 10):
#         print(f'{j} X {i} = {i * j}', end='\t\t')
#     print()

#############################################################

# print(*('\t'.join([f'{j} X {i} = {i * j}' for j in range(2, 6)]) for i in range(2, 11) ), sep = '\n', end = '\n\n')
# print(*('\t'.join([f'{j} X {i} = {i * j}' for j in range(6, 10)]) for i in range(2, 11) ), sep = '\n')

#############################################################

# print(*(f'{j} X {i} = {i * j}\t' if j%5 !=0 else f'{i} X {j} = {i * j}\n'  for i in range(2, 11) for j in range(2, 6)))

############################################################

def simple_generator(n):
    count = 0
    current = 2
    while count < n:
        flag = True
        for i in range(2, current//2+1):
            if not current % i:
                flag = False
        current += 1
        if flag:
            count += 1
            yield current-1

generator = simple_generator(int(input("Введите число  ")))

print(*generator)