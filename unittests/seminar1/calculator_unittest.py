import unittest
from seminar1.calculator import Calculator


def seminar_test():
    if 8 != Calculator.calculation(2, 6, '+'):
        raise AssertionError("Ошибка в методе")

    if 0 != Calculator.calculation(2, 2, '-'):
        raise AssertionError("Ошибка в методе")

    if 14 != Calculator.calculation(2, 7, '*'):
        raise AssertionError("Ошибка в методе")

    if 2 != Calculator.calculation(100, 50, '/'):
        raise AssertionError("Ошибка в методе")

    try:
        Calculator.calculation(8, 4, '_')
    except:
        AssertionError("Ошибка в методе")

    assert 8 == Calculator.calculation(2, 6, '+')
    assert 0 == Calculator.calculation(2, 2, '-')
    assert 14 == Calculator.calculation(2, 7, '*')
    assert 2 == Calculator.calculation(100, 50, '/')


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.calculation(2, 6, '+'), 8)

    def test_subtract(self):
        self.assertEqual(self.calculator.calculation(2, 2, '-'), 0)

    def test_multiply(self):
        self.assertEqual(self.calculator.calculation(2, 7, '*'), 14)

    def test_divide(self):
        self.assertEqual(self.calculator.calculation(100, 50, '/'), 2)

    def test_EqualZeroError(self):
        self.assertEqual(self.calculator.calculating_discount(100, 15), 85)

    def test_purchase_less_than_discount(self):
        self.assertEqual(self.calculator.calculating_discount(100, 101), -1)


if __name__ == "__main__":
    seminar_test()
    unittest.main()
