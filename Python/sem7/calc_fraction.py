from fractions import Fraction as F


def calc_fraction_main(a, b, move):
    if move == '+':
        return F(a) + F(b)
    if move == '-':
        return F(a) - F(b)
    if move == '*':
        return F(a) * F(b)
    if move == '/':
        return F(a) / F(b)
