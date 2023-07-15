

# Оказалось hasattr выдает True на все типы данных, зато obj.__hash__ выдает None для нехешируемых

def func(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if value.__hash__ is None:
            print(value)
            value = str(value)
        result[value] = key
    return result

print(func(a=5, b = 'string', c = ['l', 'i', 's', 't'], d = ('t', 'u','p', 'l', 'e'), e = {'s', 'e', 't'} ))