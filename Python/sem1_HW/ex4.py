num = int(input('Введите номер четверти >>> '))
if num == 1:
    print(f'X > 0, Y > 0')
elif num == 2:
    print(f'X < 0, Y > 0')
elif num == 3:
    print(f'X < 0, Y < 0')
elif num == 4:
    print(f'X > 0, Y < 0')
else:
    print('Я так не играю')