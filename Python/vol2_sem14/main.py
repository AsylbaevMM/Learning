import doctest


class MatrixError(Exception):
    pass


class NotRectangularMatrixError(MatrixError):
    def __init__(self, matrix):
        self._matrix = matrix

    def __str__(self):
        return f"Это не прямоугольная матрица! Длины строк матрицы: {', '.join(str(len(i)) for i in self._matrix)}."


class MatrixAddSizeError(MatrixError):
    def __init__(self, matrix_1, matrix_2):
        self._matrix_1 = matrix_1
        self._matrix_2 = matrix_2

    def __str__(self):
        return f"Для сложения матрицы должны быть одинакового размера! \
Размеры полученных матриц: {self._matrix_1.rows}x{self._matrix_1.cols}, {self._matrix_2.rows}x{self._matrix_2.cols}."


class MatrixMulSizeError(MatrixError):
    def __init__(self, matrix_1, matrix_2):
        self._matrix_1 = matrix_1
        self._matrix_2 = matrix_2

    def __str__(self):
        return f"Умножение матриц невозможно! \
Число столбцов первой матрицы ({self._matrix_1.cols}) должно быть равно числу строк второй матрицы ({self._matrix_2.rows})."


class Matrix:
    '''
    >>> print(Matrix([[1,2,3], [4, 5, 6], [7, 8, 9]]) + Matrix([[9,8,7], [6,5,4], [3,2,1]]))
     10 10 10
     10 10 10
     10 10 10
    >>> print(Matrix([[1,2], [3,4], [5, 6]]) * Matrix([[1, 2, 3], [4, 5, 6]]))
      9 12 15
     19 26 33
     29 40 51
    >>> print(Matrix([[1,2,3], [4, 5, 6], [7, 8, 9]]) == Matrix([[1,2,3], [4, 5, 6], [7, 8, 9]]))
    True
    >>> print(Matrix([[1,2,3], [4, 5, 6], [7, 8, 9]]) != Matrix([[1,2,3], [4, 5, 6], [7, 8, 9]]))
    False
    >>> matrix = Matrix([[1,2,3], [4, 5, 6], [7, 8]])
    Traceback (most recent call last):
    ...
    NotRectangularMatrixError: Это не прямоугольная матрица! Длины строк матрицы: 3, 3, 2.
    >>> print(Matrix([[1,2], [3,4], [5, 6]]) * Matrix([[1, 2, 3], [4, 5, 6], [4, 7, 8]]))
    Traceback (most recent call last):
    ...
    MatrixMulSizeError: Умножение матриц невозможно! Число столбцов первой матрицы (2) должно быть равно числу строк второй матрицы (3).
    '''
    def __init__(self, matrix):
        if any([len(matrix[0]) != len(i) for i in matrix[1:]]):
            raise NotRectangularMatrixError(matrix)
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
                raise MatrixAddSizeError(self, other)
            temp_matrix = []
            for i in range(len(self.matrix)):
                temp_matrix.append(list(map(sum, zip(self.matrix[i], other.matrix[i]))))
            return Matrix(temp_matrix)
        return NotImplemented
    
    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.cols != other.rows:
                raise MatrixMulSizeError(self, other)
            temp_matrix = [[0] * other.cols for _ in range(self.rows)]
            for i in range(self.rows):
                for j in range(other.cols):
                    for q in range(self.cols):
                        temp_matrix[i][j] += self.matrix[i][q] * other.matrix[q][j]
            return Matrix(temp_matrix)
        return NotImplemented
 
if __name__ == "__main__":
    doctest.testmod(verbose=True)

