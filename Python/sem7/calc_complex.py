def calc_complex_main(a, b, move):
    if move == '*':
        return a * b
    if move == '/':
        return a / b
    if move == '+':
        return a + b
    if move == '-':
        return a - b

num1 = input('Введите первое число: ')
num2 = input('Введите комплексное число (Пример 4j): ')
oper = input('Введите операцию над комплексными числами: ')

calc_complex_main(num1, num2, oper)