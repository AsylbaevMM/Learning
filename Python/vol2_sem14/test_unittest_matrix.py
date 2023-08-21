import unittest
from main import *

class TestMatrix(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Matrix([[1,2,3], [4, 5, 6], [7, 8, 9]]) + Matrix([[9,8,7], [6,5,4], [3,2,1]]), \
                         Matrix([[10,10,10], [10,10,10], [10,10,10]]), msg = 'Матрицы сложились неправильно')

    def test_mul(self):
        self.assertEqual(Matrix([[1,2], [3,4], [5, 6]]) * Matrix([[1, 2, 3], [4, 5, 6]]), \
                         Matrix([[9, 12, 15], [19, 26, 33], [29, 40, 51]]), msg = 'Ошибка в умножении матриц')
        
    def test_eq(self):
        self.assertEqual(Matrix([[1,2], [3,4], [5, 6]]) == Matrix([[1,2], [3,4], [5, 6]]), True, msg = 'Проблема сравнения на равенство')

if __name__ == '__main__':
    unittest.main(verbosity=2)