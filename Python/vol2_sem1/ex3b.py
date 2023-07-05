left = 1
right = 1000
try_count = 10

while try_count:
    try_count -= 1
    middle = (left + right)//2
    print(f'Я думаю это число {middle}, если я угадал, введите все что угодно, если загаданное число больше введите +, если меньше ввведите - ')
    check = input(' >>> ')
    if check == '+':
        left = middle + 1
    elif check == '-':
        right = middle -1
    else:
        break

if try_count >= 0:
    print(f"Я угадал число {middle} за {10 - try_count} попыток!")
else:
    print('Ах ты кожаный ...')
