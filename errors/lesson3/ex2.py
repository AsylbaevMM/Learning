

def do_something():
    raise ValueError('Сообщение об ошибке')

try:
    do_something()
except ValueError as e:
    print(e)
