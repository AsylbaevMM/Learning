import pytest
from main import *

def test_add():
    assert Matrix([[1,2,3], [4, 5, 6], [7, 8, 9]]) + Matrix([[9,8,7], [6,5,4], [3,2,1]]) == Matrix([[10,10,10], [10,10,10], [10,10,10]])


def test_notRectangularError():
    with pytest.raises(NotRectangularMatrixError):
        obj = Matrix([[1,2,3], [4, 5, 6], [7, 8]])

def test_mul():
    assert Matrix([[1,2], [3,4], [5, 6]]) * Matrix([[1, 2, 3], [4, 5, 6]]) == Matrix([[9, 12, 15], [19, 26, 33], [29, 40, 51]])

if __name__ == '__main__':
    pytest.main()