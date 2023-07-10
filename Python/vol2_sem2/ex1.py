

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
result = ''

num = input('Введите целое число >>> ')

while not num.isdigit():
    num = input('Некорректный ввод. Введите целое число >>> ')

number = int(num)

while number:
    result = digits[number%16] + result
    number //= 16

print(f"Алгоритм выдал: {result}")

print(f"Функция hex выдала: {hex(int(num))[2:]}")




