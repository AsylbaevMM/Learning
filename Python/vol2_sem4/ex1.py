
def transpose(matrix):
    temp = list(list(i) for i in zip(*matrix))
    matrix.clear()
    matrix.extend(temp)



matrix = [[i*(10-j) for i in range(10)] for j in range(10)]
print(*matrix, sep = '\n')
print('-'*30)
transpose(matrix)
print(*matrix, sep = '\n')