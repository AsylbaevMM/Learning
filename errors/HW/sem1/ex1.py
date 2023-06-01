

def concat_unconcatable(array, digit):
    return array + digit

def too_deep_recursion(num):
    if num > 0:
        return too_deep_recursion(num)
    return 0

def wrong_attribute(value):
    return value.what

# Создаем TypeError при попытке сложить строку и цифру
concat_unconcatable('example', 5)

# Создаем RecursionError при неверных условиях рекурсии
too_deep_recursion(5)

# Создаем AttributeError обращаясь к несуществующему атрибуту
wrong_attribute(None)