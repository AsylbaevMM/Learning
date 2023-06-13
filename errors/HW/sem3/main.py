
from datetime import datetime as dt


def check_name(name):
    '''Проверяем, что введено три слова и там только буквы'''
    name = name.split(' ')
    return all([i.isalpha() for i in name]) and len(name) == 3

def check_birthday(day):
    '''Пробуем распарсить дату, по результату возвращаем булево значение'''
    try:
        dt.strptime(day, '%d.%m.%Y')
        return True
    except:
        return False

def check_phone(phone):
    '''Проверяем, что пришло ровно 10 цифр номера'''
    return phone.isdigit() and len(phone) == 10

def check_gender(gender):
    return gender.lower() in ['m', 'f']



def main():
    name = input('Введите Ф.И.О. >>> ')
    while not check_name(name):
        print('Некорректный ввод!')
        name = input('Введите корректные Ф.И.О. >>> ')

    birthday = input('Введите дату рождения в формате ДД.ММ.ГГГГ >>> ')
    while not check_birthday(birthday):
        print('Введена некорректная дата!')
        birthday = input('Введите корректную дату рождения в формате ДД.ММ.ГГГГ >>> ')

    phone = input('Введите ваш номер телефона >>> +7')
    while not check_phone(phone):
        print('Введен некорректный номер!')
        phone = input('Введите корректный номер телефона >>> +7')

    gender = input('ВВедите ваш пол (f/m) >>> ')
    while not check_gender(gender):
        print('Некорректный ввод!')
        gender = input('ВВедите ваш пол (f/m) >>> ')

    with open(f'{name.split()[0]}.txt', mode = 'a', encoding = 'utf-8') as file:
        file.write(f'Пользователь: {name}, дата рождения: {birthday}, Тел.:{phone}, пол: {gender}.\n')

def controller():
    print("Добро пожаловать!")
    print("Для ввода нового пользователя нажмите Enter, для выхода введите exit")
    choice = input('>>> ')
    while True:
        if choice == '':
            main()
            print("Для ввода нового пользователя нажмите Enter, для выхода введите exit")
            choice = input('>>> ')
        elif choice == 'exit':
            break
        else:
            print('Неизвестная команда')
            choice = input('Повторите ввод >>> ')
    print('До встречи!')

controller()