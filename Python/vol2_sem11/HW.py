


class Matrix:
    def __init__(self, matrix):
        if any([len(matrix[0]) != len(i) for i in matrix[1:]]):
            raise ValueError('Это не прямоугольная матрица!')
        if any([any([type(j) is not int for j in i]) for i in matrix]):
            raise ValueError('Элементы матрицы должны быть целыми числами!')
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])

    def __str__(self):
        return '\n'.join(''.join(str(j).rjust(3) for j in i) for i in self.matrix)
    
    def __repr__(self):
        return f"Matrix({self.matrix.__repr__()})"

    def __eq__(self, other):
        if isinstance(other, Matrix):
            return self.matrix == other.matrix
        return NotImplemented
    
    def __add__(self, other):
        if isinstance(other, Matrix):
            if self.rows != other.rows or self.cols != other.cols:
                raise ValueError('Для сложения матрицы должны быть одинакового размера!')
            temp_matrix = []
            for i in range(len(self.matrix)):
                temp_matrix.append(list(map(sum, zip(self.matrix[i], other.matrix[i]))))
            return Matrix(temp_matrix)
        return NotImplemented
    
    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.cols != other.rows:
                raise ValueError('Умножение матриц невозможно! Число столбцов первой матрицы должно быть равно числу строк второй матрицы.')
            temp_matrix = [[0] * other.cols for _ in range(self.rows)]
            for i in range(self.rows):
                for j in range(other.cols):
                    for q in range(self.cols):
                        temp_matrix[i][j] += self.matrix[i][q] * other.matrix[q][j]
            return Matrix(temp_matrix)
        return NotImplemented
 
matrix_1 = Matrix([[1,2,3], [4, 5, 6], [7, 8, 9]])
matrix_2 = Matrix([[9,8,7], [6,5,4], [3,2,1]])
print("matrix_1:")
print(matrix_1)
print("\nmatrix_2:")
print(matrix_2)
print("\nmatrix_1 + matrix_2:")
print(matrix_1 + matrix_2)


matrix_3 = Matrix([[1,2], [3,4], [5, 6]])
matrix_4 = Matrix([[1, 2, 3], [4, 5, 6]])

print("\nmatrix_3:")
print(matrix_3)
print("\nmatrix_4:")
print(matrix_4)
print("\nmatrix_3 * matrix_4: ")
print(matrix_3 * matrix_4  )
    
print(f"{matrix_1 != matrix_2 = }")
