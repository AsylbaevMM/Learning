from fractions import Fraction as F


num1 = input('Введите первое число >>> ')
num2 = input('Введите первое число >>> ')

numerator1, denominator1 = [int(i) for i in num1.split('/')]
numerator2, denominator2 = [int(i) for i in num2.split('/')]

#  Multiplication

multiplication = numerator1*numerator2, denominator1*denominator2

mul_result = multiplication

for i in range(2, min(multiplication)//2+1):
    if multiplication[0] % i == 0 and multiplication[1] % i == 0:
        mul_result = multiplication[0] / i, multiplication[1] / i

print(f"Результат умножения моим алгоритмом: {int(mul_result[0])}/{int(mul_result[1])}")
print(f"Результат умножения через модуль fractions: {F(num1) * F(num2)}")

# Addition

addition = numerator1*denominator2 + numerator2*denominator1, denominator1*denominator2
add_result = addition

for i in range(2, min(addition)//2+1):
    if addition[0] % i == 0 and addition[1] % i == 0:
        add_result = addition[0] / i, addition[1] / i

print(f"Результат сложения моим алгоритмом: {int(add_result[0])}/{int(add_result[1])}")
print(f"Результат сложения через модуль fractions: {F(num1) + F(num2)}")