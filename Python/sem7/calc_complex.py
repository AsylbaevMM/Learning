def calc_complex_main(a, b, move):
    a, b = complex(a), complex(b)
    if move == '*':
        return a * b
    if move == '/':
        return a / b
    if move == '+':
        return a + b
    if move == '-':
        return a - b
