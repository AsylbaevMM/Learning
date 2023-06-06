
def check_float(data):
    # Метод проверяет, что бы введенная строка содержала именно дробное число
    # На целые числа тоже будет ругаться
    try:
        result = float(data)
        return not result.is_integer()
    except:
        return False


num  = input('Введите дробное число  >>> ')

while not check_float(num):
    num  = input('Это не дробное число, повторите ввод >>> ')

print(f"Вы ввели {num}, это дробное число")