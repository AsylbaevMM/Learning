class MainHW:

    # HW 3.1. Нужно покрыть тестами метод на 100%
    # Метод проверяет, является ли целое число записанное в переменную n, чётным (true) либо нечётным (false).
    @staticmethod
    def even_odd_number(n):
        if n % 2 == 0:
            return True
        else:
            return False

    # HW 3.2. Нужно написать метод который проверяет, попадает ли переданное число в интервал (25;100) и возвращает true, если попадает и false - если нет,
    # покрыть тестами метод на 100%
    @staticmethod
    def number_in_interval(n):
        if 25 < n < 100:
            return True
        else:
            return False
