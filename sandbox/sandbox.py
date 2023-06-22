def spiral_transposition(matrix):
    n = len(matrix)
    m = len(matrix[0])
    i = 0
    j = 0

    cnt = 1
    result = []
    if not n*m:
        return result

    while cnt < n*m:
        while j < m - 1 and matrix[i][j + 1] != None:
            result.append(matrix[i][j])
            matrix[i][j] = None
            j += 1
            cnt += 1

        while i < n - 1 and matrix[i + 1][j] != None:
            result.append(matrix[i][j])
            matrix[i][j] = None
            i += 1
            cnt += 1

        while j > 0 and matrix[i][j - 1] != None:
            result.append(matrix[i][j])
            matrix[i][j] = None
            j -= 1
            cnt += 1

        while i > 0 and matrix[i - 1][j] != None:
            result.append(matrix[i][j])
            matrix[i][j] = None
            i -= 1
            cnt += 1

    result.append(matrix[i][j])
    return result


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
          
print(spiral_transposition(matrix))