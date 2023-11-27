import math


class Calculator:
    def __init__(self):
        pass

    @staticmethod
    def calculation(first_operand: int, second_operand: int, operator: chr):
        result = 0
        match operator:
            case '+':
                return first_operand + second_operand
            case '-':
                return first_operand - second_operand
            case '*':
                return first_operand * second_operand
            case '/':
                if second_operand != 0:
                    return first_operand / second_operand
                else:
                    raise ZeroDivisionError("Division by zero is not possible")
            case _:
                ValueError("Unexpected value operator: " + operator)

    @staticmethod
    def square_root_extraction(number: float):
        if number == 0:
            raise ArithmeticError("It is not possible to extract the root from 0")
        if number < 0:
            raise ArithmeticError("It is impossible to extract the root from negative numbers")
        return math.sqrt(number)

        # @ param purchase_amount сумма покупки
        # @ param discount_amount размер скидки (в процентах)
        # @ return возвращает сумму покупки с учетом скидки

    @staticmethod
    def calculating_discount(purchase_amount: float, discount_amount: int):
        return purchase_amount - purchase_amount * discount_amount / 100
