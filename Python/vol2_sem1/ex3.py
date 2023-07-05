from random import randint

num = randint(0, 1000)
try_count = 10

check = int(input(f'Введите число, попыток = {try_count} >>> '))

while check != num and try_count >= 0:
    try_count -= 1
    if check > num:
        print('Меньше')
    elif check < num:
        print('Больше')
    check = int(input(f'Введите число, попыток = {try_count} >>> '))

if try_count == 0:
    print('Не повезло')
else:
    print(f"Верно! Загаданное число: {num}")